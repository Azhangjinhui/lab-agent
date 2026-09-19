import axios from 'axios'
import { ElMessage } from 'element-plus'
import { logout, getToken } from '@/utils/auth'
import router from '@/router'

// 创建axios实例
const service = axios.create(
    {
        baseURL: import.meta.env.VITE_API_BASE_URL,
        timeout: 30000
    }
)
// 请求拦截器
service.interceptors.request.use(config => {
    const token = getToken()
    if (token) {
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
},
    (err) => {
        return Promise.reject(err)
    }
);

// 响应拦截器
service.interceptors.response.use((res) => {
    const data = res.data
    if (data.code !== 200) {
        ElMessage.error(data.message || '请求失败')
        if (data.code === 401) {
            logout()
            router.push('/login')
        }
        return Promise.reject(data)
    }
    return data
}, (err) => {
    if (err.response) {
        const httpstatuscode = err.response.status
        if (httpstatuscode === 401) {
            ElMessage.error('登录过期，请重新登录')
            logout()
            router.push('/login')
        } else {
            ElMessage.error(err.response.data.message || '请求失败')
        }
    }
    else {
        ElMessage.error('网络错误')
    }
    return Promise.reject(err)
})

export default service
