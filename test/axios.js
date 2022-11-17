 import axios from "axios"

const instance = axios.create(
    {
        baseURL: 'https://CS411-Project-backend-team-4.com'
    }
)


export default instance