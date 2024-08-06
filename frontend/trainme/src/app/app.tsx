import { Box, Container } from "@chakra-ui/react";
import { ReactNode } from "react";
import NavBar from "./components/NavBar";

export default function App({ children }: { children: ReactNode }) {
  return (
    <Box bg={"gray.100"} p={1} minH={"100vh"}>
      <Box m={4} p={4} borderRadius={"lg"} bg={"white"}>
        <NavBar />
        {children}
      </Box>
    </Box>
  );
}
