import Cookies from 'js-cookie';

export const isUserAuthenticated = () => {
  const token = Cookies.get('olimpiad_cookie');
  return !!token;
};