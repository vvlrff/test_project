import { Navigate, Outlet } from 'react-router-dom';
import { useAppDispatch, useAppSelector } from '../app/hooks';
import { selectAuth, setUser } from '../features/authSlice';
import { useEffect } from 'react';

export const ProtectedRoute = () => {
    // const { access_token } = useAppSelector(selectAuth);

    // console.log(access_token)

    const dispatch = useAppDispatch();
    const user = JSON.parse(localStorage.getItem("user") || "{}");
    console.log(user)
  
    useEffect(() => {
      dispatch(setUser(user));
    }, []);

    return (user === "{}" ? (
        <Navigate to="/auth" />
    ) : (
        <Outlet />
    ))
};