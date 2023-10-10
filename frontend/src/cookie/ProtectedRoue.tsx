import React, { ReactNode } from 'react';
import { Route, Navigate } from 'react-router-dom';
import { isUserAuthenticated } from './isUserAuthenticated ';

interface ProtectedRouteProps {
    path: string;
    element: ReactNode;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ path, element }) => {
    return (!isUserAuthenticated ? (
        <Navigate to="/auth" />
    ) : (
        <Route path={path} element={element} />
    ))
};