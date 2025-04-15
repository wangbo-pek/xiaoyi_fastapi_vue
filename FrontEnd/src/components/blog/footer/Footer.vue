<template>
    <div class="footer-container">
        <div class="copy-right">
            <div class="first-line">
                <span class="info-text">Copyright</span>
                <v-icon class="info-icon" icon="mdi-copyright"></v-icon>
                <span class="info-text">2023 - 2025 &nbsp;&nbsp;</span>
                <span class="info-text strong-text">{{ aboutMeStore.myDetail.nickname }}</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;Powered By </span>
                <span class="info-text strong-text">FastAPI + Vue</span>
            </div>
            <div class="second-line">
                <v-icon class="info-icon" icon="mdi-text-long"></v-icon>
                <span class="info-text">站点总文章数：</span>
                <span class="info-text strong-text">{{ siteInformationStore.siteFooter.blogArticleCount }}篇</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-chart-areaspline"></v-icon>
                <span class="info-text">站点总字数：</span>
                <span
                    class="info-text strong-text">{{ Math.round(siteInformationStore.siteFooter.blogWordCount / 1000) }}k 字</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-eye-outline"></v-icon>
                <span class="info-text">总访问量：</span>
                <span class="info-text strong-text">%2%人</span>
                <span class="info-text">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                <v-icon class="info-icon" icon="mdi-cloud-outline"></v-icon>
                <span class="info-text">本站已运行：</span>
                <span class="info-text strong-text">{{ siteInformationStore.siteFooter.blogExisted }}天</span>
            </div>
        </div>
        <div class="touch-me">
            <v-img class="wechat-icon" :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/wechat.svg`"
                   @click="showWechatDialog = true"></v-img>
            <v-img class="mail-icon" :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/gmail.svg`"
                   @click="touchMe('mailMe')"></v-img>
            <v-img class="rss-icon" :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/rss.svg`"
                   @click="touchMe('rssMe')"></v-img>
        </div>
    </div>

    <!-- 我的微信二维码 -->
    <v-dialog v-model="showWechatDialog" width="500">
        <v-card class="qr-card" color="#1e1e1e">
            <v-card-title class="text-center text-white">微信扫一扫</v-card-title>
            <v-card-text class="text-center">
                <v-img
                    :src="aboutMeStore.myDetail.wechatQR"
                    aspect-ratio="1"
                    contain
                />
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="rgb(242, 204, 15)" @click="showWechatDialog = false">关闭</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup lang='ts'>
    import useSiteInformationStore from "@/store/blog/storages/site_info.ts";
    import useAboutMeStore from "@/store/blog/storages/about_me.ts";
    import useNoteStore from "@/store/blog/storages/note.ts";
    import useDiaryStore from "@/store/blog/storages/diary.ts";
    import {ref, watch} from "vue";
    import dayjs from "dayjs";

    defineOptions({
        name: 'Footer',
        inheritAttrs: false
    })
    const showWechatDialog = ref(false)
    let aboutMeStore = useAboutMeStore()
    let siteInformationStore = useSiteInformationStore()
    let noteStore = useNoteStore()
    let diaryStore = useDiaryStore()


    const touchMe = (name: string) => {
        const urlMap: Record<string, string> = {
            mailMe: 'mailto:wangbo.pek@gmail.com',
            rssMe: ''
        }
        const url = urlMap[name]
        if (url) {
            window.open(url, '_blank')
        }
    }

    watch([noteStore.noteList, diaryStore.diaryList, siteInformationStore.siteInformation], () => {
        // 设置博客footer的数据
        siteInformationStore.siteFooter.blogArticleCount = noteStore.noteList.length + diaryStore.diaryList.length
        siteInformationStore.siteFooter.blogViewCount = 0
        siteInformationStore.siteFooter.blogExisted = dayjs().diff(dayjs(siteInformationStore.siteInformation.createdTime), 'days')
        noteStore.noteList.forEach((value) => {
            siteInformationStore.siteFooter.blogWordCount += value.wordCount
        })
    })
</script>

<style scoped lang='scss'>
    .footer-container {
        background-color: rgba(0, 23, 26, 0.75);
        border-top: 1px solid rgba(0, 100, 100, 0.5);
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;

        .copy-right {
            width: 50%;


            .first-line,
            .second-line,
            .third-line {
                color: rgba(255, 255, 255, 0.75);
                width: 100%;
                max-width: 750px;
                text-align: left;
                padding: 5px;
                box-sizing: border-box;
                font-size: 0.75rem;
            }

            .first-line {
                margin: 30px 5px 5px 5px;
            }

            .second-line {
                margin-bottom: 30px;
            }

            .info-text {
                vertical-align: middle;
                font-size: 0.85rem;
            }

            .info-icon {
                font-size: 0.7rem;
                position: relative;
                top: 1px;
                margin: 0 2px;
            }

            .strong-text {
                font-weight: 800;
            }
        }

        .touch-me {
            display: flex;
            justify-content: left;
            align-items: center;
            width: 15%;

            .wechat-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }

            .mail-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }

            .rss-icon {
                margin: 0 15px 0 15px;
                max-width: 1.8rem;
                cursor: pointer;
            }
        }
    }

    .qr-card {
        border-radius: 12px;
        padding: 1rem;

        .v-card-title {
            font-size: 1.2rem;
            font-weight: bold;
        }

        .v-card-text img {
            border-radius: 8px;
            max-width: 100%;
        }
    }

</style>