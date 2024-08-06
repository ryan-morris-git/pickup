import {
  Button,
  Image,
  Text,
  ButtonGroup,
  Card,
  CardBody,
  CardFooter,
  Divider,
  Heading,
  Stack,
} from "@chakra-ui/react";

export default function SportCard({ details }: { details: any }) {
  const { name, sport, location, cost } = details;

  return (
    <Card size={"lg"} cursor={"pointer"} onClick={() => console.log(details._id)}>
      <CardBody>
        <Image
          src={`/sports_img/${sport}.jpg`}  
          alt="Green double couch with wooden legs"
          borderRadius="lg" 
        />
        <Stack mt="6" spacing="3">
          <Heading size="sm">
            Learn {sport} with {name}
          </Heading>
          <Text>{location}</Text>
          <Text color="blue.600" fontSize="2xl">
            {cost === 0 ? "Free" : `$${cost}`}
          </Text>
        </Stack>
      </CardBody>
    </Card>
  );
}
