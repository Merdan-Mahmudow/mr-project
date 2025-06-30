import { Fieldset, Stack, Field, Input, NativeSelect, For, Button, HStack, VStack } from '@chakra-ui/react'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/login')({
  component: RouteComponent,
  
})

function RouteComponent() {
  return (
    <HStack h={"full"}>
      <VStack w={"full"}>
        <Fieldset.Root size="lg" maxW="md" textAlign={"center"} alignItems={"center"} display={"flex"} flexDir={"column"}>
          <Stack>
            <Fieldset.Legend>Contact details</Fieldset.Legend>
            <Fieldset.HelperText>
              Please provide your contact details below.
            </Fieldset.HelperText>
          </Stack>

          <Fieldset.Content>
            <Field.Root>
              <Field.Label>Name</Field.Label>
              <Input name="name" />
            </Field.Root>

            <Field.Root>
              <Field.Label>Email address</Field.Label>
              <Input name="email" type="email" />
            </Field.Root>

            <Field.Root>
              <Field.Label>Country</Field.Label>
              <NativeSelect.Root>
                <NativeSelect.Field name="country">
                  <For each={["United Kingdom", "Canada", "United States"]}>
                    {(item) => (
                      <option key={item} value={item}>
                        {item}
                      </option>
                    )}
                  </For>
                </NativeSelect.Field>
                <NativeSelect.Indicator />
              </NativeSelect.Root>
            </Field.Root>
          </Fieldset.Content>

          <Button type="submit" alignSelf="flex-start">
            Submit
          </Button>
        </Fieldset.Root>
      </VStack>
    </HStack>
  )
}
