import { Container } from "@chakra-ui/react";
import TrainerGrid from "./components/TrainingsGrid";
import getTrainers from "./services/getTrainers";

import { useEffect, useState } from "react";

export default async function Home() {
  const trainings = await getTrainers();

  return (
    <Container minH={"80vh"} maxW={"80vw"} p={4}>
      <TrainerGrid trainings={trainings} />
    </Container>
  );
}
