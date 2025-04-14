import {defineStore} from "pinia";
import type {SiteInformation} from "@/store/types/site_info.ts";


const useSiteInformationStore = defineStore('siteInformation', {
    state: () => {
        return {
            siteInformation: {
                "siteName": '',
                "siteSubtitle": '',
                "logoUrl": '',
                "faviconUrl": '',
                "icpNumber": '',
                "publicSecurity": '',
                "githubUrl": '',
                "keywords": '',
                "description": '',
                "createdTime": '',
                "wechatSponsorQR": '',
                "alipaySponsorQR": '',
            } as SiteInformation
        }
    }
})

export default useSiteInformationStore