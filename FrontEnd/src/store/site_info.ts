import {defineStore} from "pinia";
import type {SiteInformation, SiteSocialLink} from "@/store/types/site_info.ts";


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
            } as SiteInformation,
            siteFooter:{
                "blogArticleCount":0,
                "blogWordCount":0,
                "blogViewCount":0,
                "blogExisted":0
            },
            siteSocialLinkList:[] as SiteSocialLink[]
        }
    }
})

export default useSiteInformationStore