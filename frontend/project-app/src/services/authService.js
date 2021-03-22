import axios from 'axios';
import { formValues } from 'redux-form';
import { AuthUrls } from '../constants/urls';
import { headers } from '../utils/headers';

export const signUpService = (formValues) => {
    return axios.post(AuthUrls.SIGN_UP, formValues, headers);
}; 

export const signInService = (formValues) => {
    return axios.post(AuthUrls.SIGN_IN, formValues, headers)
            .then((response) => {
                if (response.data.token) {
                    localStorage.setItem("user", JSON.stringify(response.data));
                }
                return response.data;
            })
};

export const signOutService = () => {
    localStorage.removeItem("user");
};