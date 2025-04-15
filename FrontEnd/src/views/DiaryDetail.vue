<template>
    <div class="header-container">
        <div class="header" :class="{'change-bgcolor':isScrollOverViewport}">
            <div class="title-big">
                <HeaderTitle></HeaderTitle>
            </div>
            <div class="nav-big">
                <HeaderNav></HeaderNav>
            </div>
            <div class="widget-big">
                <HeaderWidget></HeaderWidget>
            </div>
        </div>
    </div>

    <div class="coverImage" ref="coverImageRef"
         :style="{ backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.2)), url(${diaryStore.currentDiary.coverImg})`,
         filter: 'blur(1px)'}"></div>

    <div class="title-container">
        <span class="diary-title">{{ diaryStore.currentDiary.title }}</span>
    </div>

    <div class="content-container">
        <div class="diary-background">
            <div class="create-time-and-tags">
                <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                <span class="created-date-text">{{ diaryStore.currentDiary.createdTime }}</span>
                <span class="tag" v-for="(tag, index) in diaryStore.currentDiary.tags" :key="index">
                    #{{ tag.name }}
                </span>
            </div>

            <div class="tags-container">
            </div>

            <div class="body-container">
                <div class="diary-body markdown-content" v-html="diaryStore.currentDiary.renderedMarkdown"></div>
            </div>
        </div>
    </div>

    <div class="coffee-container">
        <span class="coffee-text">COFFEE ME &nbsp;</span>
        <v-img class="coffee-icon"
               :src="'https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/coffee.svg'"></v-img>
    </div>

    <div class="divider3"></div>

    <v-icon class="back-icon" icon="mdi-arrow-left" @click="backTo"></v-icon>

</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useDiaryStore from "@/store/diary.ts";
    import {useRouter} from "vue-router";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/header/HeaderNav.vue";
    import HeaderTitle from "@/components/header/HeaderTitle.vue";
    import HeaderWidget from "@/components/header/HeaderWidget.vue";
    import MarkdownIt from "markdown-it";
    import hljs from "highlight.js";
    import 'highlight.js/styles/github.css'

    defineOptions({
        name: 'DiaryDetail',
        inheritAttrs: false
    })

    const route = useRoute()
    const diaryStore = useDiaryStore()
    const diaryListId = Number(route.params.id)
    const $router = useRouter()
    const md = new MarkdownIt({html: true})

    let coverImageRef = ref<HTMLElement | null>(null)
    let isScrollOverViewport = ref(false)
    const handleScroll = () => {
        if (coverImageRef.value) {
            let rect = coverImageRef.value.getBoundingClientRect()
            isScrollOverViewport.value = rect.bottom <= 55
        }
    }

    // 解析并高亮代码块
    const highlightCode = () => {
        const codeBlock = document.querySelectorAll('pre code')
        codeBlock.forEach((block) => {
            hljs.highlightElement(block as HTMLElement)
        })
    }

    onMounted(() => {
        // 页面加载时，从后端获取日记content
        axios_server.get(`/api/diary/${diaryListId}`).then(
            (response) => {
                const currentDiaryList = diaryStore.diaryList.find((value) => {
                    return value.diaryListId == diaryListId
                })
                Object.assign(diaryStore.currentDiary, currentDiaryList, response.data)

                // 将markdown进行渲染
                diaryStore.currentDiary.renderedMarkdown = md.render(diaryStore.currentDiary.markdownContent)
            }
        )

        // 调用highlightCode处理代码高亮
        highlightCode()

        // 监听handleScroll
        window.addEventListener('scroll', handleScroll)
        const rect = coverImageRef.value!.getBoundingClientRect()
        isScrollOverViewport.value = rect.bottom <= 55
    })

    onUnmounted(() => {
        window.removeEventListener('scroll', handleScroll)
    })

    // 实时渲染markdown
    watchEffect(() => {
        if (diaryStore.currentDiary.renderedMarkdown) {
            setTimeout(() => {
                highlightCode()
            }, 100)
        }
    })

    const backTo = () => {
        $router.back()
    }
</script>

<style scoped lang='scss'>
    .header-container {
        padding: 0;
        margin: 0;
        position: fixed;
        width: 100%;
        height: 8vh;
        z-index: 1000;

        .header {
            display: flex;
            justify-content: center;
            align-items: stretch;
            height: 100%;
            width: 100%;
            background-color: rgba(100, 100, 100, 0.1);

            .title-big {
                width: 35%;
                height: 100%;
                padding-right: 30px;
            }

            .nav-big {
                width: 35%;
                height: 100%;
            }

            .widget-big {
                width: 30%;
                height: 100%;
            }
        }

        .change-bgcolor {
            background-color: rgba(0, 14, 16, 0.75);
            border-bottom: 1px solid rgba(0, 100, 100, 0.5);
        }
    }

    .coverImage {
        width: 100%;
        height: 50vh;
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        background-position-x: 10%;
        background-position-y: 80%;
        filter: brightness(0.5);
    }

    .title-container {
        .diary-title {
            width: 100%;
            padding: 20px 200px 5px 200px;
            border-radius: 10px 10px 2px 0;
            position: absolute;
            top: 20.2rem;
            font-size: 4rem;
            background-color: rgba(0, 75, 57, 0.5);
            color: #ffffff;
            text-align: center;
        }
    }

    .content-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;

        .diary-background {
            padding: 50px 80px 20px 80px;
            width: 75%;
            position: relative;
            top: -2em;

            .create-time-and-tags {
                display: flex;
                align-items: center;
                gap: 10px;

                .created-date-icon {
                    color: #d6faec;
                    font-size: 1.1rem;
                }

                .created-date-text {
                    color: #d6faec;
                    font-size: 1.1rem;
                }

                .tag{
                    margin-left: 20px;
                    color: #d6faec;
                    font-size: 1.1rem;
                }
            }

            .body-container {
                display: flex;
                justify-content: center;
                align-items: flex-start;

                .diary-body {
                    width: 100%;
                    padding: 15px 25px;
                    border-radius: 12px;
                }
            }
        }
    }

    .coffee-container {
        position: relative;
        top: -10px;
        display: flex;
        justify-content: center;
        align-items: center;

        .coffee-icon {
            max-width: 2.5%;
        }

        .coffee-text {
            color: #c3effa;
            font-size: 1rem;
            font-weight: 800;
        }
    }

    .divider3 {
        position: relative;
        top: -2px;
        display: flex;
        width: 100%;
        height: 2px;
        background-color: #515c7a;;
        margin: 50px 0 100px 0;
    }

    .back-icon {
        position: fixed;
        top: 1rem;
        left: 3rem;
        color: white;
        font-size: 2rem;
        z-index: 3000;
    }

    @import "@/styles/markdown";
    :deep(.markdown-content) {
    }

    :deep(.toc) {
    }
</style>