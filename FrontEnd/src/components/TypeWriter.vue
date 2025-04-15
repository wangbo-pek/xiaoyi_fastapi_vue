<template>
    <div class="typewriter">
        <span class="text">{{ displayedText }}</span><span class="cursor"></span>
    </div>
</template>

<script setup lang='ts'>
    import {watch, ref} from "vue";
    import type {TypingWriter} from "@/store/types/writer.ts";
    import useAboutMeStore from "@/store/about_me.ts";

    defineOptions({
        name: 'TypeWriter',
        inheritAttrs: false
    })

    const aboutMeStore = useAboutMeStore()
    const props = defineProps<TypingWriter>()
    const displayedText = ref('“人的一生就应该像一条河，开始是涓涓细流，被狭窄的河岸所束缚，然后，它激烈地奔过巨石，冲越瀑布。渐渐地，河流变宽了，两边的堤岸也远去，河水流动得更加平静。最后，它自然地融入了大海，并毫无痛苦地消失了自我。” —— 伯特兰·罗素')
    const isDeleting = ref(false)
    let timeoutId: ReturnType<typeof setTimeout> | null = null

    watch(() => props.text, () => {
        reset()
        startTyping()
    })

    // 监听App.aboutMeStore.myDetail，如果拿到了就开始typing
    watch(() => aboutMeStore.myDetail.wisdom, () => {
        startTyping()
    })

    function reset() {
        displayedText.value = ''
        isDeleting.value = false
        if (timeoutId) {
            clearTimeout(timeoutId)
            timeoutId = null
        }
    }

    function startTyping() {
        let i = 0

        const type = () => {
            const fullText = props.text
            const typingSpeed = props.typingSpeed ?? 100
            const deletingSpeed = props.deletingSpeed ?? 50
            const pauseTime = props.pauseTime ?? 1500

            if (!isDeleting.value) {
                displayedText.value = fullText.slice(0, i++)
                if (i > fullText.length) {
                    isDeleting.value = true
                    timeoutId = setTimeout(type, pauseTime)
                    return
                }
            } else {
                displayedText.value = fullText.slice(0, i--)
                if (i < 0) {
                    isDeleting.value = false
                    i = 0
                    timeoutId = setTimeout(type, pauseTime)
                    return
                }
            }
            timeoutId = setTimeout(type, isDeleting.value ? deletingSpeed : typingSpeed)
        }
        type()
    }

</script>

<style scoped lang='scss'>
    .typewriter {
        font-weight: 800;
        font-size: 1.3rem;
        color: rgba(250, 250, 250, 0.9);
        white-space: normal;
        word-break: break-word;
        display: inline-block;
        line-height: 2rem;
    }

    .cursor {
        display: inline-block;
        width: 2px;
        height: 1.2rem;
        background-color: white;
        margin-left: 2px;
        animation: blink 1s steps(2, start) infinite;
    }

    @keyframes blink {
        0%, 100% {
            opacity: 1
        }
        50% {
            opacity: 0
        }
    }
</style>