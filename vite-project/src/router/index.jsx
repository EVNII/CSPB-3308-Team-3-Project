import { createBrowserRouter, Outlet } from 'react-router-dom'
import Login from '../pages/login'
import Home from '../pages/home'
import NavBar from '../components/ui/NavBar';
import UserProfile from '../pages/userProfile';
import UserList from '../pages/userList';
import Signup from '../pages/signup';
import ScoreList from '../pages/ScoreList';
import ScoreDetail from '../pages/scoreDetail';
import UserEdit from '../pages/userEdit';

export const globalRouters = createBrowserRouter([{
    element: (
        <>
            <NavBar />
            <Outlet />
        </>
    ),
    children: [{
        path: '/login',
        element: <Login />,
    },
    {
        path: '/signup',
        element: <Signup />,
    },
    {
        path: '/user/:id',
        element: <UserProfile />,
    },
    {
        path: '/user/',
        element: <UserList />,
    },
    {
        path: '/user/edit',
        element: <UserEdit />,
    },
    {
        path: '/score',
        element: <ScoreList />,
    },
    {
        path: '/score/:id',
        element: <ScoreDetail />,
    },
    {
        path: '/',
        element: <Home />,
    },]
}
]);