// 对axios进行二次封装
import axios from "axios";

let axios_server = axios.create({
    baseURL: 'http://localhost:8000/',
    timeout: 10000,
    withCredentials: true
})

// 获取浏览器中保存的csrf_token的cookie
function getCsrfToken(): string | undefined {
    const cookies = document.cookie.split(';')
    for (const cookie of cookies) {
        const [key, value] = cookie.trim().split('=')
        if (key === 'csrftoken') {
            return value
        }
    }
    return undefined
}

// 给axios_server添加请求拦截器
axios_server.interceptors.request.use((config) => {
    console.log('config', config)
    const token = getCsrfToken()
    console.log('token', token)
    if (token) {
        config.headers['X-CSRFToken'] = token
    }
    // 必须返回配置对象
    return config
})

// 给axios_server添加响应拦截器
axios_server.interceptors.response.use(
        // 成功的回调
        (response) => {
            return response.data
        },
        // 失败的回调
        (error) => {
            console.log(error)
        }
)
export default axios_server