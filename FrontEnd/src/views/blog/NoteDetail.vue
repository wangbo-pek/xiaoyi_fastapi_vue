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
         :style="{ backgroundImage: `linear-gradient(to bottom,rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.1)), url(${noteStore.currentNote.coverImg})`,
         filter: 'blur(0.25px)'}"></div>

    <div class="article-title-container">
        <span class="article-title">{{ noteStore.currentNote.title }}</span>
    </div>

    <div class="article-content-container">
        <div class="article-background">

            <!-- 标签、分类区域 -->
            <div class="tags-category-container">
                <div class="tags-container">
                    <span class="tag" v-for="(tag, index) in noteStore.currentNote.tags" :key="index">
                        {{ tag.name }}
                    </span>
                </div>
                <div class="category-container">
                    <span class="category">
                        <v-icon class="category-icon" icon="mdi-bookmark-multiple"></v-icon>
                        <span class="category-text">{{ noteStore.currentNote.category.name }}</span>
                    </span>
                </div>
            </div>

            <!-- 创建时间、更新时间等区域 -->
            <div class="article-info-container">
                <span class="created-date">
                    <v-icon class="created-date-icon" icon="mdi-calendar-sync-outline"></v-icon>
                    <span class="created-date-text">{{ noteStore.currentNote.createdTime }}</span>
                </span>

                <span class="view">
                    <v-icon class="view-icon" icon="mdi-eye-outline"></v-icon>
                    <span class="view-text">{{ noteStore.currentNote.viewCount }}</span>
                </span>

                <span class="like">
                    <v-icon class="like-icon" icon="mdi-heart-outline"></v-icon>
                    <span class="like-text">{{ noteStore.currentNote.likeCount }}</span>
                </span>
                <span class="dislike">
                    <v-icon class="dislike-icon" icon="mdi-heart-off-outline"></v-icon>
                    <span class="dislike-text">{{ noteStore.currentNote.dislikeCount }}</span>
                </span>

                <span class="word_count">
                        <v-icon class="word_count-icon" icon="mdi-ab-testing"></v-icon>
                        <span class="word_count-text">{{ noteStore.currentNote.wordCount }}字</span>
                    </span>

                <span class="reading-time">
                        <v-icon class="reading-time-icon" icon="mdi-clock-outline"></v-icon>
                        <span class="reading-time-text">{{ noteStore.currentNote.readingTime }}分钟</span>
                    </span>
            </div>

            <div class="divider1"></div>

            <!-- 文章正文区域 -->
            <div class="article-body-container">
                <div class="article-body markdown-content" v-html="noteStore.currentNote.renderedMarkdown"></div>
            </div>

            <!-- toc内容 -->
            <div class="toc markdown-content">
                <div class="toc-title">
                    <v-icon class="toc-title-icon" icon="mdi-table-of-contents"></v-icon>
                    <span class="toc-title-text">目录</span>
                </div>
                <div v-html="toc"></div>
            </div>

            <div class="like-dislike-container">
                <template v-if="likeStatus==='liked'">
                    <div class="like-dislike">
                        <span class="liked-text">Thanks a lot for your kind encouragement! </span>
                    </div>
                    <div class="like-dislike-icon">
                        <v-icon class="liked-icon"
                                icon="mdi-heart"
                                @click="updateNoteStatistic('undoLike')"
                        ></v-icon>
                        <v-icon class="dislike-icon"
                                icon="mdi-heart-off-outline"
                                @click="updateNoteStatistic('undoLike')"
                        ></v-icon>
                    </div>
                </template>

                <template v-else-if="likeStatus==='disliked'">
                    <div class="like-dislike">
                        <span class="disliked-text">Copied that. It means a lot to me, thank you! </span>
                    </div>
                    <div class="like-dislike-icon">
                        <v-icon class="like-icon"
                                icon="mdi-heart"
                                @click="updateNoteStatistic('undoDislike')"
                        ></v-icon>
                        <v-icon class="disliked-icon"
                                icon="mdi-heart-off"
                                @click="updateNoteStatistic('undoDislike')"
                        ></v-icon>
                    </div>
                </template>

                <template v-else-if="likeStatus==='default'">
                    <div class="like-dislike">
                        <span class="like-dislike-text">Can this article be praised? </span>
                    </div>
                    <div class="like-dislike-icon">
                        <v-icon class="like-icon"
                                icon="mdi-heart-outline"
                                @click="updateNoteStatistic('like')"
                        ></v-icon>
                        <v-icon class="dislike-icon"
                                icon="mdi-heart-off-outline"
                                @click="updateNoteStatistic('dislike')"
                        ></v-icon>
                    </div>
                </template>

            </div>

            <div class="divider2"></div>

            <!-- 文章footer区域 -->
            <div class="article-footer-container">
                <div class="author-container">
                    <span class="author">
                        <v-icon class="author-icon" icon="mdi-account-outline"></v-icon>
                        <span class="author-text">文章作者：WangBo</span>
                    </span>
                </div>
                <div class="link-container">
                    <span class="link">
                        <v-icon class="link-icon" icon="mdi-link"></v-icon>
                        <span class="link-text">文章链接：https://127.0.0.1:8001/article/2</span>
                    </span>
                </div>
                <div class="copy-right-container">
                    <span class="copy-right">
                        <v-icon class="copy-right-icon" icon="mdi-copyright"></v-icon>
                        <span class="copy-right-text">版权声明：本博客所有文章除特別声明外，均采用 CC BY 4.0 许可协议。转载请注明来源 WangBo</span>
                    </span>
                </div>
            </div>

            <!-- 文章外部link区域 -->
            <div class="share-container">
                <div class="tags">
                    <span class="tag" v-for="(tag, index) in noteStore.currentNote.tags"
                          :key="index">{{ tag.name }}</span>
                </div>
                <div class="social-icon-container">
                    <template v-for="item in siteInformationStore.siteSocialLinkList" :key="item.socialName">
                        <v-img class="social-icon" :src="item.socialFaviconUrl"
                               @click="jumpToSocialMedia(item)"></v-img>
                    </template>
                </div>
            </div>

            <div class="coffee-container" @click="showCoffeeDialog = true">
                <span class="coffee-text">Coffee Me </span>
                <v-img class="coffee-icon"
                       :src="`https://xiaoyi-blog.oss-cn-beijing.aliyuncs.com/svg_icons/coffee.svg`"></v-img>
            </div>
        </div>
    </div>

    <div class="recommend-note-container"></div>

    <v-dialog v-model="showCoffeeDialog" width="800">
        <v-card class="qr-card" color="#1e1e1e">
            <v-card-title class="text-center text-white">感谢您的支持!</v-card-title>
            <v-card-text class="text-center">
                <div style="display: flex; justify-content: center; gap: 20px;">
                    <v-img
                        :src="siteInformationStore.siteInformation.alipaySponsorQR"
                        aspect-ratio="1"
                        max-width="40%"
                    />
                    <v-img
                        :src="siteInformationStore.siteInformation.wechatSponsorQR"
                        aspect-ratio="1"
                        max-width="40%"
                    />
                </div>
            </v-card-text>
            <v-card-actions class="justify-center">
                <v-btn color="rgb(242, 204, 15)" @click="showCoffeeDialog = false">关闭</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

    <v-icon class="back-icon" icon="mdi-arrow-left" @click="backTo"></v-icon>
</template>

<script setup lang='ts'>
    import {useRoute} from "vue-router";
    import {nextTick, onMounted, onUnmounted, ref, watchEffect} from "vue";
    import useSiteInformationStore from "@/store/blog/storages/site_info.ts";
    import useNoteStore from "@/store/blog/storages/note.ts";
    import {useRouter} from "vue-router";
    import axios_server from "@/utils/axios_server.ts";
    import HeaderNav from "@/components/blog/header/HeaderNav.vue";
    import HeaderTitle from "@/components/blog/header/HeaderTitle.vue";
    import HeaderWidget from "@/components/blog/header/HeaderWidget.vue";
    import MarkdownIt from 'markdown-it';
    import hljs from 'highlight.js'
    import 'highlight.js/styles/github.css'
    import type {SiteSocialLink} from "@/store/blog/types/site_info.ts";
    import type {NoteListItem} from "@/store/blog/types/note.ts";


    defineOptions({
        name: 'NoteDetail',
        inheritAttrs: false
    })

    const route = useRoute()
    const noteStore = useNoteStore()
    const siteInformationStore = useSiteInformationStore()
    const noteListId = Number(route.params.id)
    const $router = useRouter()

    // 获取class="coverImage"的DOM
    let coverImageRef = ref<HTMLElement | null>(null)
    // 是否滚动过封面区域
    let isScrollOverViewport = ref(false)
    // 滚动监听函数
    const handleScroll = () => {
        if (coverImageRef.value) {
            let rect = coverImageRef.value.getBoundingClientRect()
            isScrollOverViewport.value = rect.bottom <= 55
        }
    }

    const md = new MarkdownIt({
        html: true,
        linkify: true, // 识别纯链接如 https://xxx.com
        typographer: true // 美化排版符号，如引号等
    })

    // 重写 link_open 渲染逻辑，添加 target 和 rel
    md.renderer.rules.link_open = (tokens, idx, options, env, renderer) => {
        const token = tokens[idx]
        console.log(env)
        // 如果没有 target="_blank"，就添加
        const targetIndex = token.attrIndex('target')
        if (targetIndex < 0) {
            token.attrPush(['target', '_blank'])
        } else {
            token.attrs![targetIndex][1] = '_blank'
        }

        // 添加 rel="noopener noreferrer"（防止 window.opener 漏洞）
        const relIndex = token.attrIndex('rel')
        if (relIndex < 0) {
            token.attrPush(['rel', 'noopener noreferrer'])
        } else {
            token.attrs![relIndex][1] = 'noopener noreferrer'
        }

        return renderer.renderToken(tokens, idx, options)
    }

    // 前端展示table of contents的内容
    const toc = ref('')

    const handleTableOfContents = () => {
        const rendered = noteStore.currentNote.renderedMarkdown
        const headingRegex = /<(h[1-2])>(.*?)<\/h[1-2]>/g

        let match
        let updatedMarkdown = rendered
        let tocHtml = ''
        let h1Index = 0
        let h2Index = 0

        const tocItems: { level: string, text: string, id: string }[] = []

        // 收集所有 heading（顺序重要）
        while ((match = headingRegex.exec(rendered)) !== null) {
            const level = match[1]
            const text = match[2]

            if (level === 'h1') {
                h1Index++
                h2Index = 0
                const id = `heading-${h1Index}`
                tocItems.push({level, text, id})
                updatedMarkdown = updatedMarkdown.replace(match[0], `<h1 id="${id}">${text}</h1>`)
            } else if (level === 'h2') {
                h2Index++
                const id = `heading-${h1Index}-${h2Index}`
                tocItems.push({level, text, id})
                updatedMarkdown = updatedMarkdown.replace(match[0], `<h2 id="${id}">${text}</h2>`)
            }
        }

        // 构建结构良好的嵌套 HTML
        tocHtml += '<ul>'
        let openSublist = false

        tocItems.forEach((item, index) => {
            if (item.level === 'h1') {
                // 关闭之前的子列表
                if (openSublist) {
                    tocHtml += '</ul>'
                    openSublist = false
                }
                tocHtml += `<li><a href="#${item.id}">${item.text}</a>`
                // 检查后面是否有 h2
                if (tocItems[index + 1]?.level === 'h2') {
                    tocHtml += '<ul>'
                    openSublist = true
                } else {
                    tocHtml += '</li>'
                }
            } else if (item.level === 'h2') {
                tocHtml += `<li><a href="#${item.id}">${item.text}</a></li>`
                // 如果下一个不是 h2，关闭当前子列表
                if (tocItems[index + 1]?.level !== 'h2') {
                    tocHtml += '</ul></li>'
                    openSublist = false
                }
            }
        })

        if (openSublist) {
            tocHtml += '</ul></li>'
        }

        tocHtml += '</ul>'

        noteStore.currentNote.renderedMarkdown = updatedMarkdown
        toc.value = tocHtml
    }

    const jumpToSocialMedia = (social: SiteSocialLink) => {
        window.open(social.socialUrl, '_blank')
    }

    const backTo = () => {
        $router.back()
    }

    // 控制咖啡图片 dialog
    const showCoffeeDialog = ref(false)

    // 控制like-icon、dislike-icon的状态
    let likeStatus = ref<'liked' | 'disliked' | 'default'>('default')
    const updateNoteStatistic = (action: string) => {
        // 在store中获取当前noteListId的noteList的索引，用于更新like_count和dislike_count
        let noteListIndex = -1
        noteStore.noteList.find((value: NoteListItem, index) => {
            noteListIndex = index
            return value.noteListId == noteListId
        })
        if (action === 'like') {  // likeStatus是default时，点击了like-icon
            axios_server.patch('/api/note/update_note_statistic', {
                noteListId,
                action
            }).then(() => {
                likeStatus.value = 'liked'
                noteStore.currentNote.likeCount += 1
                noteStore.noteList[noteListIndex].likeCount += 1
            })
        } else if (action === 'dislike') {  // likeStatus是default时，点击了dislike-icon
            axios_server.patch('/api/note/update_note_statistic', {
                noteListId,
                action
            }).then(() => {
                likeStatus.value = 'disliked'
                noteStore.currentNote.dislikeCount += 1
                noteStore.noteList[noteListIndex].dislikeCount += 1
            })
        } else if (action === 'undoLike') {  // likeStatus是liked时，点击了like-icon或dislike-icon
            axios_server.patch('/api/note/update_note_statistic', {
                noteListId,
                action
            }).then(() => {
                likeStatus.value = 'default'
                noteStore.currentNote.likeCount -= 1
                noteStore.noteList[noteListIndex].likeCount -= 1
            })
        } else if (action === 'undoDislike') {  // likeStatus是disliked时，点击了like-icon或dislike-icon
            axios_server.patch('/api/note/update_note_statistic', {
                noteListId,
                action
            }).then(()=>{
                likeStatus.value = 'default'
                noteStore.currentNote.dislikeCount -= 1
                noteStore.noteList[noteListIndex].dislikeCount -= 1
            })
        }
    }

    onMounted(async () => {
        // 页面加载时，从后端获取文章content
        axios_server.get(`/api/note/${noteListId}`).then(
            (response) => {
                const currentNoteList = noteStore.noteList.find((value: NoteListItem) => {
                    return value.noteListId == noteListId
                })
                Object.assign(noteStore.currentNote, currentNoteList, response.data)

                // 将markdown进行渲染
                noteStore.currentNote.renderedMarkdown = md.render(noteStore.currentNote.markdownContent)
                // 调用 handleTableOfContents 来处理table of contents
                handleTableOfContents()
            }
        )

        // 调用 highlightCode 来处理代码高亮
        highlightCode()

        // 页面挂载时监听handleScroll
        window.addEventListener('scroll', handleScroll)
        const rect = coverImageRef.value!.getBoundingClientRect()
        isScrollOverViewport.value = rect.bottom <= 55

        setTimeout(() => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            })
        }, 10)

        // toc可以平滑滚动
        document.documentElement.classList.add('smooth-scroll')
    })

    onUnmounted(() => {
        // 页面卸载时移除监听
        window.removeEventListener('scroll', handleScroll)
    })

    const highlightCode = () => {
        console.log("📋 highlightCode 执行了")
        const blocks = document.querySelectorAll('pre code')

        blocks.forEach((codeBlock) => {
            const pre = codeBlock.parentElement
            if (!pre || pre.classList.contains('code-decorated')) return

            // 避免重复处理
            pre.classList.add('code-decorated')

            // === 创建容器结构 ===
            const wrapper = document.createElement('div')
            wrapper.className = 'code-wrapper'

            const header = document.createElement('div')
            header.className = 'code-header'


            // 获取语言 class，如 language-python
            const langClass = Array.from(codeBlock.classList).find(cls => cls.startsWith('language-'))
            const langLabel = langClass ? langClass.replace('language-', '') : ''
            // ✅ 创建语言标签 DOM
            const langSpan = document.createElement('span')
            langSpan.className = 'code-lang'
            langSpan.textContent = langLabel.toUpperCase()

            const macDots = document.createElement('div')
            macDots.className = 'mac-dots'
            macDots.innerHTML = `
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
        `

            const copyBtn = document.createElement('button')
            copyBtn.className = 'copy-btn'
            copyBtn.innerHTML = `
  <svg class="copy-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#ccc" viewBox="0 0 24 24">
    <path d="M0 0h24v24H0z" fill="none"/>
    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
  </svg>
`
            copyBtn.addEventListener('click', () => {
                navigator.clipboard.writeText(codeBlock.textContent || '')
                copyBtn.textContent = '已复制'
                setTimeout(() => copyBtn.innerHTML = `
  <svg class="copy-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#ccc" viewBox="0 0 24 24">
    <path d="M0 0h24v24H0z" fill="none"/>
    <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
  </svg>
`, 1500)
            })

            // ✅ 添加到 header 中
            header.appendChild(macDots)
            header.appendChild(langSpan)
            header.appendChild(copyBtn)
            header.appendChild(copyBtn)

            // 替换 DOM 结构：把 pre 放进 wrapper
            const parent = pre.parentElement!
            parent.insertBefore(wrapper, pre)
            wrapper.appendChild(header)
            wrapper.appendChild(pre)
            hljs.highlightElement(codeBlock as HTMLElement)
        })
    }

    watchEffect(() => {
        if (noteStore.currentNote.renderedMarkdown) {
            nextTick(() => {
                highlightCode()
            })
        }
    })
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
            background-color: rgba(100, 100, 100, 0.25);

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
        width: 85%;
        height: 65vh;
        margin: 0 auto;
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
        background-position-x: 10%;
        background-position-y: 80%;
    }

    .article-title-container {

        .article-title {
            width: 100%;
            padding: 20px 200px 5px 200px;
            border-radius: 2px;
            position: absolute;
            top: 25rem;
            font-size: 4rem;
            background-color: rgba(0, 75, 57, 0.25);
            color: #ffffff;
            text-align: center;
            line-height: 5rem;
        }
    }

    .article-content-container {
        display: flex;
        justify-content: center;
        align-items: flex-start;

        .article-background {
            padding: 50px 80px 20px 80px;
            width: 75%;
            position: relative;
            top: -1em;

            .tags-category-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 12px;

                .tags-container {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;

                    .tag {
                        background-color: rgba(0, 75, 57);
                        color: white;
                        padding: 8px 12px;
                        border-radius: 5px;
                        font-size: 0.9rem;
                        font-weight: 800;
                    }
                }

                .category-container {

                    .category {
                        padding: 8px 12px;
                        border-radius: 5px;
                        background-color: white;
                        display: flex;
                        align-items: center;
                        gap: 5px;

                        .category-icon {
                            font-size: 0.9rem;
                            color: rgba(0, 75, 57);
                        }

                        .category-text {
                            font-size: 0.8rem;
                            font-weight: 800;
                            color: rgba(0, 75, 57);
                        }
                    }
                }
            }

            .article-info-container {
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                margin: 30px 0 10px 0;

                .created-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .created-date-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1.2rem;
                    }

                    .created-date-text {
                        color: rgb(20, 200, 150);
                        font-size: 1.1rem;
                        font-weight: 800;
                    }
                }

                .updated-date {
                    display: flex;
                    align-items: center;
                    gap: 4px;

                    .updated-date-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .updated-date-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }
                }

                .view {
                    display: flex;
                    align-items: center;
                    gap: 5px;

                    .view-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .view-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }
                }

                .like {
                    display: flex;
                    align-items: center;
                    gap: 5px;

                    .like-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .like-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                }

                .dislike {
                    display: flex;
                    align-items: center;
                    gap: 5px;

                    .dislike-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .dislike-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                }

                .word_count {
                    display: flex;
                    align-items: center;
                    gap: 5px;

                    .word_count-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .word_count-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }
                }

                .reading-time {
                    display: flex;
                    align-items: center;
                    gap: 5px;

                    .reading-time-icon {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }

                    .reading-time-text {
                        color: rgb(20, 200, 150);
                        font-size: 1rem;
                    }
                }
            }

            .divider1 {
                width: 100%;
                height: 2px;
                background-color: rgba(0, 75, 57);
                margin: 10px 0 10px 0;
            }

            .article-body-container {
                display: flex;
                justify-content: center;
                align-items: flex-start;

                .article-body {
                    width: 100%; // 控制文章宽度
                    padding: 15px 25px; // 设置内边距
                    border-radius: 12px; // 给背景添加圆角效果
                }
            }

            .like-dislike-container {
                display: flex;
                flex-direction: column;

                .like-dislike {
                    margin: 5px auto 5px auto;

                    .like-dislike-text {
                        color: white;
                    }

                    .liked-text {
                        color: white;
                    }

                    .disliked-text {
                        color: white;
                    }
                }

                .like-dislike-icon {
                    display: flex;
                    margin: 5px auto 5px auto;
                    gap: 20px;

                    .like-icon {
                        cursor: pointer;
                        color: white;
                        font-size: 1.3rem;
                    }

                    .liked-icon {
                        cursor: pointer;
                        color: red;
                        font-size: 1.3rem;
                    }

                    .dislike-icon {
                        cursor: pointer;
                        color: white;
                        font-size: 1.3rem;
                    }

                    .disliked-icon {
                        cursor: pointer;
                        color: red;
                        font-size: 1.3rem;
                    }
                }
            }

            .divider2 {
                width: 100%;
                height: 2px;
                background-color: rgba(0, 75, 57);
                margin: 20px 0 20px 0;
            }

            .article-footer-container {
                padding: 15px;
                border-radius: 5px;
                box-shadow: 1px 2px 3px rgba(138, 185, 168, 0.3);
                margin: 30px 0 20px 0;
                background-color: rgba(0, 75, 57, 0.15);;
                border: 1px solid rgba(0, 75, 57);;

                .author-container {
                    .author {
                        display: flex;
                        align-items: center;
                        gap: 1px;
                        margin: 15px;

                        .author-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .author-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }

                .link-container {
                    .link {
                        display: flex;
                        align-items: center;
                        gap: 2px;
                        margin: 15px;

                        .link-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .link-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }

                .copy-right-container {
                    .copy-right {
                        display: flex;
                        align-items: center;
                        gap: 4px;
                        margin: 15px;

                        .copy-right-icon {
                            color: rgb(10, 90, 110);
                            font-size: 0.9em;
                        }

                        .copy-right-text {
                            color: rgb(10, 110, 90);
                            font-size: 0.85em;
                            font-weight: 800;
                        }
                    }
                }
            }

            .share-container {
                position: relative;
                display: flex;
                justify-content: space-evenly;
                align-items: center;
                padding: 20px 0 20px 0;

                .tags {
                    width: 30%;
                    display: flex;
                    justify-content: flex-start;
                    gap: 10px;
                    position: relative;
                    top: -20px;
                    left: -30px;

                    .tag {
                        background-color: rgba(0, 75, 57);
                        color: white;
                        padding: 6px 10px;
                        border-radius: 5px;
                        font-size: 0.8em;
                        font-weight: 800;
                    }
                }

                .social-icon-container {
                    width: 55%;
                    display: flex;
                    justify-content: flex-end;
                    position: relative;
                    top: -12px;
                    left: 50px;

                    .social-icon {
                        margin: 0 15px 15px 0;
                        max-width: 5%;
                        cursor: pointer;
                    }
                }
            }

            .coffee-container {
                position: relative;
                top: -10px;
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: pointer;

                .coffee-icon {
                    max-width: 3%;
                }

                .coffee-text {
                    color: rgb(204, 255, 246);
                    font-size: 1.2rem;
                    font-weight: 800;
                }
            }
        }
    }

    .divider3 {
        position: relative;
        top: -75px;
        display: flex;
        width: 100%;
        height: 2px;
        background-color: #515c7a;;
        margin: 10px 0 10px 0;
    }

    @import "@/styles/markdown";
    :deep(.markdown-content) {
    }

    :deep(.toc) {
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

    .back-icon {
        position: fixed;
        top: 1rem;
        left: 3rem;
        color: white;
        font-size: 2rem;
        z-index: 3000;
    }

</style>
<style lang="scss">
    html {
        scroll-behavior: smooth;
    }
</style>