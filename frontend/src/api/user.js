





/**
 * 获取用户信息
 */
import request from '@/utils/request'


export function getUserInfo() {
    return request({
        url:'/api/user/info',
        method:'get',
    })
}

export function updateUserInfo(data) {
    return request({
        url:'/api/user/update',
        method:'put',
        data
    })  
}
export function updatePasswordApi(data) {
    return request({
        url:'/api/user/updatepassword',
        method:'put',
        data
    })
}

