import axios from 'axios'

const getAPI = axios.create({
    baseURL: '127.0.0.1:5000',
})

export { getAPI }