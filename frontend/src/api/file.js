import request from '@/utils/request'

/**
 * 上传文件
 * @param {File} file 待上传的文件对象
 */
export function uploadFileApi(file) {
    const formData = new FormData()
    formData.append('file', file)
    return request({
        url: '/api/file/upload',
        method: 'post',
        data: formData
    })
}
