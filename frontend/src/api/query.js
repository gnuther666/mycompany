import {fetchPost, fetchGet} from './http'

export function ApiGetBriefUserList (p) {
  return fetchGet('/User/user_list', p)
}

export function ApiGetUiserDetil (p) {
  return fetchGet('/User/user_detil', p)
}

export function ApiPostBriefUser (p) {
  return fetchPost('/company1/User', p)
}
