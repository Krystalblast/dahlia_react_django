import axios from "axios";

import { AuthTypes } from "../constants/actionTypes";
import { AuthUrls } from "../constants/urls";
import store from "../store";


export function getUserToken(state) {
    return state.auth.token;
}