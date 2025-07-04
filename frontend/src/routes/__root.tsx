import { createRootRoute } from '@tanstack/react-router'
import { TanStackRouterDevtools } from '@tanstack/react-router-devtools'
import Layout from './_layout'

export const Route = createRootRoute({
    component: () => (
        <>
            <Layout />
            <TanStackRouterDevtools />
        </>
    ),
})