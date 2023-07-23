import { createBrowserRouter, Outlet } from 'react-router-dom'
import Login from '../pages/login'
import Home from '../pages/home'
import NavBar from '../components/ui/NavBar';

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
        path: '/',
        element: <Home />,
    },]
}
]);