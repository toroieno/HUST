import { USE_MOCK_DATA } from '../config'
import FakeApi from '@/api/FakeApi'
import Api from '@/api/Api'

const debug = process.env.NODE_ENV !== 'production'
const test = process.env.NODE_ENV === 'testing'

const useMock = test || (USE_MOCK_DATA && debug)

let api
if (useMock) {
  api = new FakeApi()
} else {
  api = new Api()
}

export default api
