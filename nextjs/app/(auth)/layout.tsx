import { ClerkProvider } from "@clerk/nextjs"
import { Inter } from "next/font/google"
import '../globals.css'

export const metadata = {
  title: 'storyai',
  description: 'A AI generated Story Application'
}

const inter = Inter({ subsets: ["latin"] })

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
  <ClerkProvider>
    <html lang="en"> 
      <body className={`${inter.className} bg-dark-a`}>
       {children}
      </body>
    </html>
  </ClerkProvider>
  )
}
