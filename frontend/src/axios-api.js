import axios from 'axios';

const getAPI = axios.create({
	baseURL: 'http://ec2-52-2-8-51.compute-1.amazonaws.com',
	timeout: 5000,
})

export { getAPI}