import { AuthTypes} from "../constants/actionTypes";

export function authReducer(state = {}, action) {
    switch(action.type) {
        case AuthTypes.SIGN_IN:
            return { ...state, authenticated: true, token: action.payload};
        case AuthTypes.SIGN_OUT:
            return { ...state, authenticated: false, token: null};
        case AuthTypes.USER_PROFILE:
            return { ...state, user: action.payload};
    }
    return state;
}

