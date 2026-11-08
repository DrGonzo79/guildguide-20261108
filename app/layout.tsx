import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"GuildGuide — maintained buying guides",description:"A fictional workflow for expert-reviewed community buying guides."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
