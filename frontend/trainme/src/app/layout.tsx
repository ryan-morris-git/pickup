import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import NavBar from "./components/NavBar";
import { ChakraProvider } from "@chakra-ui/react";
import App from "./app";
const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Train Me",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ChakraProvider>
          <App>{children}</App>
        </ChakraProvider>
      </body>
    </html>
  );
}
