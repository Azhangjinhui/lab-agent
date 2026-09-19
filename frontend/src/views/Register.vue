<template>
  <div class="register-container">
    <!-- 左侧：卡通角色区 -->
    <div class="characters-panel" @mousemove="handleMouseMove">
      <div class="logo">
        <div class="logo-icon">🧭</div>
        <span class="logo-text">智能实验室预约系统</span>
      </div>

      <div class="characters-stage">
        <!-- 橙色半圆角色 -->
        <div class="character orange" :class="{ active: activeField }" ref="orangeRef">
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(0, 0)">
              <div class="pupil" :class="{ closed: activeField === 'password' }"></div>
            </div>
            <div class="eye" :style="getEyeStyle(0, 1)">
              <div class="pupil" :class="{ closed: activeField === 'password' }"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 紫色矩形角色 -->
        <div class="character purple" :class="{ active: activeField }" ref="purpleRef">
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(1, 0)">
              <div class="pupil"></div>
            </div>
            <div class="eye" :style="getEyeStyle(1, 1)">
              <div class="pupil"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 黑色矩形角色 -->
        <div class="character black" :class="{ active: activeField }" ref="blackRef">
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(2, 0)">
              <div class="pupil"></div>
            </div>
            <div class="eye" :style="getEyeStyle(2, 1)">
              <div class="pupil"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>

        <!-- 黄色圆角矩形角色 -->
        <div class="character yellow" :class="{ active: activeField }" ref="yellowRef">
          <div class="eyes">
            <div class="eye" :style="getEyeStyle(3, 0)">
              <div class="pupil"></div>
            </div>
            <div class="eye" :style="getEyeStyle(3, 1)">
              <div class="pupil"></div>
            </div>
          </div>
          <div class="mouth" :class="mouthClass"></div>
        </div>
      </div>
    </div>

    <!-- 右侧：注册表单 -->
    <div class="form-panel">
      <div class="form-card" :class="{ 'shake': registerError }">
        <h1 class="form-title">创建账号</h1>
        <p class="form-subtitle">填写以下信息完成注册</p>

        <form @submit.prevent="handleRegister">
          <!-- 账号 -->
          <div class="form-group">
            <label>账号</label>
            <input
              type="text"
              v-model="form.account"
              placeholder="请输入账号"
              @focus="setActiveField('account')"
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
                placeholder="请输入密码（至少6位）"
                @focus="setActiveField('password')"
                @blur="setActiveField(null)"
                class="form-input"
              />
              <button type="button" class="toggle-password" @click="togglePassword">
                <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
              </button>
            </div>
          </div>

          <!-- 确认密码 -->
          <div class="form-group">
            <label>确认密码</label>
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="form.confirmPassword"
              placeholder="请再次输入密码"
              @focus="setActiveField('password')"
              @blur="setActiveField(null)"
              class="form-input"
            />
            <p v-if="passwordMismatch" class="error-tip">两次输入的密码不一致</p>
          </div>

          <!-- 按钮 -->
          <button type="submit" class="btn btn-primary" :disabled="isLoading">
            {{ isLoading ? '注册中...' : '注 册' }}
          </button>
        </form>

        <p class="login-link">
          已有账号？<a href="/login" class="link">去登录</a>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const form = reactive({ account: '', password: '', confirmPassword: '' })
const activeField = ref(null)
const showPassword = ref(false)
const isLoading = ref(false)
const registerError = ref(false)
const registerSuccess = ref(false)
const mouse = reactive({ x: 0, y: 0 })

const orangeRef = ref(null)
const purpleRef = ref(null)
const blackRef = ref(null)
const yellowRef = ref(null)

const setActiveField = (field) => { activeField.value = field }

const togglePassword = () => { showPassword.value = !showPassword.value }

const handleMouseMove = (e) => {
  const rect = e.currentTarget.getBoundingClientRect()
  mouse.x = e.clientX - rect.left
  mouse.y = e.clientY - rect.top
}

const getEyeStyle = (charIndex, eyeIndex) => {
  const refs = [orangeRef, purpleRef, blackRef, yellowRef]
  const charEl = refs[charIndex].value
  if (!charEl) return {}

  const rect = charEl.getBoundingClientRect()
  const eyes = charEl.querySelectorAll('.eye')
  if (!eyes[eyeIndex]) return {}

  const charCenterX = rect.left + rect.width / 2
  const charCenterY = rect.top + rect.height / 2

  let deltaX = mouse.x + rect.left - charCenterX
  let deltaY = mouse.y + rect.top - charCenterY

  if (activeField.value) {
    deltaX = 150
    deltaY = 50
  }

  const angle = Math.atan2(deltaY, deltaX)
  const distance = Math.min(6, Math.hypot(deltaX, deltaY) * 0.05)

  return {
    transform: `translate(${Math.cos(angle) * distance}px, ${Math.sin(angle) * distance}px)`
  }
}

const mouthClass = computed(() => {
  if (registerSuccess.value) return 'happy'
  if (registerError.value) return 'sad'
  if (activeField.value) return 'curious'
  return 'neutral'
})

const passwordMismatch = computed(() => {
  return form.confirmPassword && form.password !== form.confirmPassword
})

const handleRegister = async () => {
  if (!form.account || !form.password || !form.confirmPassword) return
  if (form.password !== form.confirmPassword) return

  isLoading.value = true
  registerError.value = false
  registerSuccess.value = false

  await new Promise(resolve => setTimeout(resolve, 1200))

  if (form.password.length < 6) {
    registerError.value = true
    isLoading.value = false
    setTimeout(() => { registerError.value = false }, 600)
  } else {
    registerSuccess.value = true
    isLoading.value = false
    setTimeout(() => {
      registerSuccess.value = false
      form.account = ''
      form.password = ''
      form.confirmPassword = ''
    }, 2000)
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.register-container {
  display: flex;
  min-height: 100vh;
  font-family: 'Segoe UI', system-ui, sans-serif;
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
  background: rgba(255, 255, 255, 0.2);
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
  padding-bottom: 4rem;
  position: relative;
}

.character {
  position: relative;
  transition: transform 0.3s ease;
  margin-right: -30px;
}

.character:last-child {
  margin-right: 0;
}

.character.active {
  transform: translateX(10px) rotate(5deg);
}

/* 橙色半圆 */
.orange {
  width: 150px;
  height: 150px;
  background: #fb923c;
  border-radius: 75px 75px 0 0;
  transform-origin: bottom center;
  z-index: 4;
  margin-left: -75px;
}

.orange.active {
  transform: translateX(15px) rotate(-5deg) scale(1.02);
}

/* 紫色矩形 */
.purple {
  width: 130px;
  height: 230px;
  background: #8b5cf6;
  border-radius: 12px;
  transform-origin: bottom center;
  z-index: 1;
  order: -1;
}

.purple.active {
  transform: translateX(10px) rotate(8deg) scale(1.05);
}

/* 黑色矩形 */
.black {
  width: 95px;
  height: 195px;
  background: #1f2937;
  border-radius: 8px;
  transform-origin: bottom center;
  z-index: 2;
  margin-left: -40px;
}

.black.active {
  transform: translateX(12px) rotate(-3deg);
}

/* 黄色圆角矩形 */
.yellow {
  width: 125px;
  height: 175px;
  background: #fde047;
  border-radius: 62px 62px 16px 16px;
  transform-origin: bottom center;
  z-index: 3;
  margin-left: -35px;
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
  0%, 100% { transform: translateX(0); }
  20%, 60% { transform: translateX(-8px); }
  40%, 80% { transform: translateX(8px); }
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

.error-tip {
  margin-top: 6px;
  font-size: 0.8125rem;
  color: #ef4444;
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

.login-link {
  text-align: center;
  margin-top: 2rem;
  color: #6b7280;
  font-size: 0.875rem;
}

/* 响应式 */
@media (max-width: 768px) {
  .register-container {
    flex-direction: column;
  }

  .characters-panel {
    min-height: 300px;
  }

  .characters-stage {
    padding-bottom: 2rem;
  }

  .orange { width: 100px; height: 100px; border-radius: 50px 50px 0 0; margin-left: -50px; }
  .purple { width: 80px; height: 140px; }
  .black { width: 70px; height: 120px; }
  .yellow { width: 90px; height: 110px; border-radius: 45px 45px 12px 12px; }

  .form-panel {
    padding: 1.5rem;
  }
}
</style>