import { Navigate, Outlet } from 'react-router-dom';
import { useAppDispatch } from '../app/hooks';
import { setUser } from '../features/authSlice';
import { useEffect } from 'react';

export const ProtectedRoute = () => {
    const dispatch = useAppDispatch();
    const user = JSON.parse(localStorage.getItem("user") || "{}");
      
    useEffect(() => {
      dispatch(setUser(user));
    }, []);

    return (user === "{}" ? (
        <Navigate to="/auth" />
    ) : (
        <Outlet />
    ))
};