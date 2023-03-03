/**
 * Convert to form data
 *
 * @param {Object} data
 */
export default function toFormData (data) {
  const formData = new window.FormData()

  for (const key in data) {
    formData.append(key, data[key])
  }

  return formData
}
