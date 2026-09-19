<template>
  <div class="login-container">
    <!-- 左侧：卡通角色区 -->
    <div class="characters-panel" @mousemove="handleMouseMove">
      <div class="logo">
        <img class="logo-icon" src="@/assets/imgs/logo.png" alt="" />
        <span class="logo-text">实验室预约系统</span>
      </div>

      <div class="characters-stage">
        <!-- 橙色半圆角色（活泼开朗） -->
        <div
          class="character orange"
          :class="{ active: activeField, peeking: showPassword }"
          ref="orangeRef"
        >
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(0, 0)">
              <div
                class="pupil"
                :class="{ closed: activeField === 'password' && !showPassword }"
              ></div>
            </div>
            <div class="eye" :style="getEyeStyle(0, 1)">
              <div
                class="pupil"
                :class="{ closed: activeField === 'password' && !showPassword }"
              ></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 紫色矩形角色（傲娇） -->
        <div
          class="character purple"
          :class="{ active: activeField }"
          ref="purpleRef"
        >
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(1, 0)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
            <div class="eye" :style="getEyeStyle(1, 1)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 黑色矩形角色（冷静） -->
        <div
          class="character black"
          :class="{ active: activeField }"
          ref="blackRef"
        >
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(2, 0)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
            <div class="eye" :style="getEyeStyle(2, 1)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 黄色圆角矩形角色（温和） -->
        <div
          class="character yellow"
          :class="{ active: activeField }"
          ref="yellowRef"
        >
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(3, 0)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
            <div class="eye" :style="getEyeStyle(3, 1)">
              <div class="pupil" :class="{ closed: showPassword }"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>
      </div>
    </div>

    <!-- 右侧：登录表单 -->
    <div class="form-panel">
      <div class="form-card" :class="{ shake: loginError }">
        <h1 class="form-title">欢迎回来！</h1>
        <p class="form-subtitle">请输入您的登录信息</p>

        <form @submit.prevent="handleLogin">
          <!-- 账号 -->
          <div class="form-group">
            <label>账号</label>
            <input
              type="text"
              v-model="form.account"
              placeholder="请输入账号"
              @focus="setActiveField('email')"
              @blur="setActiveField(null)"
              class="form-input"
            />
          </div>

          <!-- 密码 -->
          <div class="form-group">
            <label>密码</label>
            <div class="password-wrapper">
              <input
                :type="showPassword ? 'text' : 'password'"
                v-model="form.password"
                placeholder="请输入密码"
                @focus="setActiveField('password')"
                @blur="setActiveField(null)"
                class="form-input"
              />
              <button
                type="button"
                class="toggle-password"
                @click="togglePassword"
                :title="showPassword ? 'Hide' : 'Show'"
              >
                <svg
                  v-if="showPassword"
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
              </button>
            </div>
          </div>

          <!-- Options -->
          <div class="form-options">
            <label class="checkbox-label">
              <input type="checkbox" v-model="form.remember" />
              <span>30天内记住我</span>
            </label>
            <a href="#" class="link">忘记密码？</a>
          </div>

          <!-- Buttons -->
          <button type="submit" class="btn btn-primary" :disabled="isLoading">
            {{ isLoading ? "登录中..." : "登 录" }}
          </button>

          <button type="button" class="btn btn-secondary">
            <svg
              class="google-icon"
              width="18"
              height="18"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
                fill="#4285F4"
              />
              <path
                d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
                fill="#34A853"
              />
              <path
                d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
                fill="#FBBC05"
              />
              <path
                d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
                fill="#EA4335"
              />
            </svg>
            使用 Google 登录
          </button>
        </form>

        <p class="signup-link">
          还没有账号？<router-link to="/register" class="link"
            >立即注册</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";
import { loginApi } from "@/api/auth";
import { useUser } from "@/utils/user";
const router = useRouter();

const form = reactive({ account: "", password: "", remember: false });
const activeField = ref(null);
const showPassword = ref(false);
const isLoading = ref(false);
const loginError = ref(false);
const loginSuccess = ref(false);
const mouse = reactive({ x: 0, y: 0 });

const orangeRef = ref(null);
const purpleRef = ref(null);
const blackRef = ref(null);
const yellowRef = ref(null);

const setActiveField = (field) => {
  activeField.value = field;
};

const togglePassword = () => {
  showPassword.value = !showPassword.value;
};

const handleMouseMove = (e) => {
  const rect = e.currentTarget.getBoundingClientRect();
  mouse.x = e.clientX - rect.left;
  mouse.y = e.clientY - rect.top;
};

const getEyeStyle = (charIndex, eyeIndex) => {
  const refs = [orangeRef, purpleRef, blackRef, yellowRef];
  const charEl = refs[charIndex].value;
  if (!charEl) return {};

  const rect = charEl.getBoundingClientRect();
  const eyes = charEl.querySelectorAll(".eye");
  if (!eyes[eyeIndex]) return {};

  const eyeRect = eyes[eyeIndex].getBoundingClientRect();
  const charCenterX = rect.left + rect.width / 2;
  const charCenterY = rect.top + rect.height / 2;

  let deltaX = mouse.x + rect.left - charCenterX;
  let deltaY = mouse.y + rect.top - charCenterY;

  // 输入框激活时聚焦右侧
  if (activeField.value) {
    deltaX = 150;
    deltaY = 50;
  }

  const angle = Math.atan2(deltaY, deltaX);
  const distance = Math.min(6, Math.hypot(deltaX, deltaY) * 0.05);

  return {
    transform: `translate(${Math.cos(angle) * distance}px, ${Math.sin(angle) * distance}px)`,
  };
};

const mouthClass = computed(() => {
  if (loginSuccess.value) return "happy";
  if (loginError.value) return "sad";
  if (activeField.value) return "curious";
  return "neutral";
});
const { saveLoginData } = useUser();
const handleLogin = async () => {
  if (!form.account || !form.password) return;
  isLoading.value = true;
  loginError.value = false;
  loginSuccess.value = false;

  try {
    const res = await loginApi({
      username: form.account,
      password: form.password,
    });
    // 保存登录态
    saveLoginData(res.data);
    loginSuccess.value = true;
    setTimeout(() => {
      router.push("/manager/home");
    }, 600);
  } catch {
    // 错误提示由 request.js 拦截器统一弹出，这里只做页面反馈
    loginError.value = true;
    setTimeout(() => {
      loginError.value = false;
    }, 600);
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.login-container {
  display: flex;
  min-height: 100vh;
  font-family: "Segoe UI", system-ui, sans-serif;
  background: #f3f4f6;
}

/* 左侧角色区 */
.characters-panel {
  flex: 1;
  background: linear-gradient(135deg, #9ca3af 0%, #6b7280 100%);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  padding: 2rem;
}

.logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: white;
  font-weight: 600;
  font-size: 1.25rem;
}

.logo-icon {
  width: 32px;
  height: 32px;

  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}

.characters-stage {
  flex: 1;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 2rem;
  padding-bottom: 4rem;
  position: relative;
}

.character {
  position: relative;
  transition: transform 0.3s ease;
}

.character.active {
  transform: translateX(10px) rotate(5deg);
}

/* 橙色半圆 - 活泼 */
.orange {
  width: 140px;
  height: 140px;
  background: #fb923c;
  border-radius: 70px 70px 0 0;
  transform-origin: bottom center;
  z-index: 4;
  margin-left: -75px;
}

.orange.active {
  transform: translateX(15px) rotate(-5deg) scale(1.02);
}

.orange.peeking .pupil {
  transform: scaleY(0.3);
  transition: transform 0.2s;
}

/* 紫色矩形 - 傲娇 */
.purple {
  width: 110px;
  height: 200px;
  background: #8b5cf6;
  border-radius: 12px;
  transform-origin: bottom center;
  z-index: 1;
  order: -1;
}

.purple.active {
  transform: translateX(10px) rotate(8deg) scale(1.05);
}

/* 黑色矩形 - 冷静 */
.black {
  width: 90px;
  height: 180px;
  background: #1f2937;
  border-radius: 6px;
  transform-origin: bottom center;
}

.black.active {
  transform: translateX(12px) rotate(-3deg);
}

/* 黄色圆角矩形 - 温和 */
.yellow {
  width: 120px;
  height: 150px;
  background: #fde047;
  border-radius: 20px;
  transform-origin: bottom center;
}

.yellow.active {
  transform: translateX(8px) rotate(6deg) scale(1.03);
}

/* 眼睛 */
.eyes {
  display: flex;
  justify-content: center;
  gap: 16px;
  padding-top: 20px;
}

.eye {
  width: 16px;
  height: 16px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.1s ease-out;
}

.pupil {
  width: 6px;
  height: 6px;
  background: #1f2937;
  border-radius: 50%;
  transition: transform 0.2s;
}

.pupil.closed {
  transform: scaleY(0.2);
  border-radius: 2px;
}

/* 嘴巴 */
.mouth {
  width: 30px;
  height: 12px;
  margin: 20px auto 0;
  border-radius: 0 0 30px 30px;
  border: 2.5px solid #1f2937;
  border-top: none;
  border-left: none;
  border-right: none;
  transition: all 0.3s;
  position: relative;
}

.mouth::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100%;
  height: 100%;
}

.mouth.neutral {
  width: 20px;
  height: 2px;
  background: #1f2937;
  border: none;
  border-radius: 2px;
}

.mouth.curious {
  width: 24px;
  height: 12px;
  border-radius: 0 0 24px 24px;
  border: 2.5px solid #1f2937;
  border-top: none;
}

.mouth.happy {
  width: 36px;
  height: 16px;
  border-radius: 0 0 36px 36px;
  border: 3px solid #1f2937;
  border-top: none;
  background: #1f2937;
}

.mouth.sad {
  width: 24px;
  height: 10px;
  border-radius: 24px 24px 0 0;
  border: 2.5px solid #1f2937;
  border-bottom: none;
  transform: rotate(180deg);
  margin-top: 24px;
}

/* 右侧表单区 */
.form-panel {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: #fff;
}

.form-card {
  width: 100%;
  max-width: 400px;
}

.form-card.shake {
  animation: shake 0.5s;
}

@keyframes shake {
  0%,
  100% {
    transform: translateX(0);
  }
  20%,
  60% {
    transform: translateX(-8px);
  }
  40%,
  80% {
    transform: translateX(8px);
  }
}

.form-title {
  font-size: 2rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.5rem;
  letter-spacing: -0.5px;
}

.form-subtitle {
  color: #6b7280;
  margin-bottom: 2.5rem;
  font-size: 0.95rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-size: 0.875rem;
  font-weight: 600;
  color: #374151;
  margin-bottom: 0.5rem;
}

.form-input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1.5px solid #e5e7eb;
  border-radius: 10px;
  font-size: 1rem;
  transition: all 0.2s;
  background: #fff;
}

.form-input:focus {
  outline: none;
  border-color: #8b5cf6;
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1);
}

.password-wrapper {
  position: relative;
}

.toggle-password {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  color: #9ca3af;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: color 0.2s;
}

.toggle-password:hover {
  color: #6b7280;
}

.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #374151;
  cursor: pointer;
  user-select: none;
}

.checkbox-label input[type="checkbox"] {
  width: 16px;
  height: 16px;
  accent-color: #8b5cf6;
  cursor: pointer;
}

.link {
  color: #8b5cf6;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: color 0.2s;
}

.link:hover {
  color: #7c3aed;
}

.btn {
  width: 100%;
  padding: 0.875rem;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  border: none;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.btn-primary {
  background: #111827;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: #1f2937;
  transform: translateY(-1px);
}

.btn-secondary {
  background: white;
  color: #374151;
  border: 1.5px solid #e5e7eb;
}

.btn-secondary:hover {
  background: #f9fafb;
  border-color: #d1d5db;
}

.google-icon {
  flex-shrink: 0;
}

.signup-link {
  text-align: center;
  margin-top: 2rem;
  color: #6b7280;
  font-size: 0.875rem;
}

/* 响应式 */
@media (max-width: 768px) {
  .login-container {
    flex-direction: column;
  }

  .characters-panel {
    min-height: 300px;
  }

  .characters-stage {
    padding-bottom: 2rem;
    gap: 1rem;
  }

  .orange {
    width: 100px;
    height: 100px;
    border-radius: 50px 50px 0 0;
  }
  .purple {
    width: 80px;
    height: 140px;
  }
  .black {
    width: 70px;
    height: 120px;
  }
  .yellow {
    width: 90px;
    height: 110px;
  }

  .form-panel {
    padding: 1.5rem;
  }
}
</style>
