import api from "@/api";
import config from "@/config.js";

export async function authLogin(data) {
  console.log('to backend', data, config.backend);
  let result = await api.post(`${config.backend}/webauthenticate`, data, {});
  console.log('end call api');
  api.setToken("Bearer " + result.data.token);
  return result;
}
