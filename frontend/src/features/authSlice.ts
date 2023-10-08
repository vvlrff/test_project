import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../app/store";

export interface AuthState {
    email: string | null;
    accessToken: string | null;
};

const initialState: AuthState = {
    email: null,
    accessToken: null
};

export const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        setUser: (
            state,
            action: PayloadAction<{ email: string, accessToken: string }>
        ) => {
            localStorage.setItem(
                "user",
                JSON.stringify({
                    email: action.payload.email,
                    accessToken: action.payload.accessToken
                })
            );
            state.email = action.payload.email;
            state.accessToken = action.payload.accessToken;
        },
        logout: (state) => {
            localStorage.clear();
            state.email = null;
            state.accessToken = null;
        },
    }
});

export const selectAuth = (state: RootState) => state.auth;

export const { setUser, logout } = authSlice.actions;

export default authSlice.reducer;