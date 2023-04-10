import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://tententranslation.com',
})

export { getAPI }