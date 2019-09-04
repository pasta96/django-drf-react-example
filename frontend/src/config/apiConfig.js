

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8000';


export const makeApiUrl = endpoint => {
    if (endpoint[0] !== '/') {
        endpoint = `/${endpoint}`;
    }
    return `${API_BASE_URL}${endpoint}`
};