<template>
    <div class="home-container">

        <div class="my-wisdom-container">
            <div class="wisdom-tab">
                My Wisdom
            </div>
            <TypeWriter
                :text="aboutMeStore.myDetail.wisdom"
                :typingSpeed="222"
            ></TypeWriter>
        </div>

        <div class="recommended-container">
            <div class="recommended-tab">
                Recommended
            </div>
            <div class="recommended-list">
                <template v-for="item in noteStore.recommendedNoteList" :key="item">
                    <Card
                        :title="item.title"
                        :bgImage="item.coverImg"
                        :createdDate="item.createdTime"
                        :category="item.category.name"
                        :tags="item.tags"
                        @click="jumpToNoteDetail(item.noteListId)"
                    ></Card>
                </template>
            </div>
        </div>

        <div class="random-note-container">
            <div class="random-note-tab">
                Latest
            </div>
            <div class="random-note-list">
                <template v-for="item in noteStore.latestNoteList" :key="item">
                    <Card
                        :title="item.title"
                        :bgImage="item.coverImg"
                        :createdDate="item.createdTime"
                        :category="item.category.name"
                        :tags="item.tags"
                        @click="jumpToNoteDetail(item.noteListId)"
                    ></Card>
                </template>
            </div>
        </div>

    </div>
</template>

<script setup lang='ts'>
    import useAboutMeStore from "@/store/blog/storages/about_me.ts";
    import useNoteStore from "@/store/blog/storages/note.ts";
    import {useRouter} from "vue-router";
    import Card from "@/components/blog/Card.vue";
    import {watch} from "vue";
    import TypeWriter from "@/components/blog/TypeWriter.vue";
    import type {NoteListItem} from "@/store/blog/types/note.ts";

    defineOptions({
        name: 'Home',
        inheritAttrs: false
    })

    const aboutMeStore = useAboutMeStore()
    const noteStore = useNoteStore()
    const $router = useRouter()

    const jumpToNoteDetail = (noteListId: number) => {
        $router.push({
            name: 'noteDetail',
            params: {
                id: noteListId
            }
        })
    }

    // 监听App.vue是否拿到了NoteList，如果拿到了，就获取被推荐的文章、最新的文章
    watch(() => noteStore.noteList, () => {
        // 获取被推荐的文章
        noteStore.recommendedNoteList = noteStore.noteList.filter((value:NoteListItem) => {
            return value.isRecommended
        })

        // 获取最新的文章
        noteStore.latestNoteList = noteStore.noteList.slice(0, 4)
    })

</script>

<style scoped lang='scss'>
    .home-container {
        height: 100%;
        border-radius: 5px;
        padding: 2px 10px;

        .my-wisdom-container {
            height: 25vh;
            background-color: transparent;
            padding: 50px;
            margin: 50px auto;
            border-radius: 20px;

            .wisdom-tab {
                color: white;
                text-align: center;
                font-size: 2rem;
                font-weight: 800;
                margin-bottom: 30px;
            }

            .my-wisdom {
                color: white;
                text-align: left;
                font-size: 1.25rem;
                font-weight: 800;
            }
        }


        .recommended-container {
            background-color: rgba(0, 35, 35, 0.2);
            padding: 50px;
            margin: 25px;
            border-radius: 20px;

            .recommended-tab {
                color: white;
                text-align: center;
                font-size: 2rem;
                font-weight: 800;
                margin-bottom: 30px;
            }

            .recommended-list {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                column-gap: 3px;
                row-gap: 20px;
                padding: 10px 20px 20px 30px;
                justify-items: center;
            }
        }

        .random-note-container {
            background-color: rgba(0, 35, 35, 0.2);
            padding: 50px;
            margin: 25px;
            border-radius: 20px;

            .random-note-tab {
                color: white;
                text-align: center;
                font-size: 2rem;
                font-weight: 800;
                margin-bottom: 30px;
            }

            .random-note-list {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                column-gap: 3px;
                row-gap: 20px;
                padding: 10px 20px 20px 30px;
                justify-items: center;
            }
        }
    }

</style>