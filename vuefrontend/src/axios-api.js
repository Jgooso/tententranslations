import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://tententranslations.com',
})

export { getAPI }