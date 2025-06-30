import { Flex } from "@chakra-ui/react"
import { Outlet, createFileRoute, useNavigate } from "@tanstack/react-router"
import { useEffect } from "react"

export const Route = createFileRoute("/_layout")({
    component: Layout,

})

function Layout() {
    const navigate = useNavigate()

    useEffect(() => {
        navigate({to: "/login"})
    }, [navigate])
    return (
        <Flex direction="column" h="100vh">
            <Flex flex="1" overflow="hidden">
                <Flex flex="1" direction="column" p={4} overflowY="auto">
                    <Outlet />
                </Flex>
            </Flex>
        </Flex>
    )
}

export default Layout
