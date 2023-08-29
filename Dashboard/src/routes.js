import { Navigate, useRoutes } from "react-router-dom";
import authRoutes from "./modules/auth/routes";
import mainRoutes from "./layouts/routes";

export const routes = [
authRoutes,
mainRoutes,
{
path: "*",
element: <Navigate to="/auth/404" replace />,
},
];

export function getRoutes(path) {
return routes.find((route) => route.path === path);
}

export default function Router() {
return useRoutes(routes);
}