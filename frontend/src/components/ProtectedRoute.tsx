import { Navigate, Outlet } from 'react-router-dom';
import { useAppSelector } from '../app/hooks';
import { selectAuth } from '../features/authSlice';

export const ProtectedRoute = () => {
    const { access_token } = useAppSelector(selectAuth);

    return (!access_token ? (
        <Navigate to="/auth"/>
    ) : (
        <Outlet />
    ))  
};