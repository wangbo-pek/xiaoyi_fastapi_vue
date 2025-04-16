// 对axios进行二次封装
import axios from "axios";

let axios_server = axios.create({
    baseURL: 'http://localhost:8000/',
    timeout: 10000,
    withCredentials: true
})

// 给axios_server添加请求拦截器
axios_server.interceptors.request.use((config) => {
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