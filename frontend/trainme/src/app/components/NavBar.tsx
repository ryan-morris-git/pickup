import { Box, Button, Flex, HStack, Spacer } from "@chakra-ui/react";

export default function NavBar() {
  return (
    <Flex m={2}>
      <HStack>
        <Box mx={2} p={4} bg={"blue.400"} />
        <Button mx={2} variant={"link"}>Locations</Button>
        <Button variant={"link"}>Sports</Button>
      </HStack>
      <Spacer />
      <HStack>
        <Button>Register</Button>
        <Button>Login</Button>
      </HStack>
    </Flex>
  );
}
