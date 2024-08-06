"use client"

import { Grid, GridItem } from "@chakra-ui/react";
import SportCard from "./SportCard";

export default function TrainerGrid({ trainings }: {trainings: any[]}) {
    console.log(trainings)
    return (
      <Grid templateColumns="repeat(5, 1fr)" gap={6}>
        {trainings.map((training: any) => (
          <GridItem key={training._id} w="100%">
            <SportCard details={training} />
          </GridItem>
        ))}
      </Grid>
    );
  }