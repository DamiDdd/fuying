<!--蒙板组件-->

<template>
    <div class="modal-bg" v-show="show" @mousemove="modalMove" @mouseup="cancelMove">
        <div class="modal-container">
            <div class="modal-header" @mousedown="setStartingPoint">
                {{ title }}
            </div>
            <div class="modal-main">
                <slot></slot>
            </div>
            <div class="modal-footer">
                <el-button round @click="hideModal">{{$t('public.cancel')}}</el-button>
                <el-button type="primary" round @click="submit">{{$t('public.confirm')}}</el-button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Modal',
    props: {
        // 控制显示的组件
        show: {
            type: Boolean,
            default: false
        },
        // 标题
        title: {
            type: String,
            default: ''
        },
    },
    data() {
        return {
            x: 0,
            y: 0,
            node: null,
            isCanMove: false
        }
    },
    mounted() {
        this.node = document.querySelector('.modal-container')
    },
    methods: {
        // 调用，隐藏蒙版
        hideModal() {
            this.$emit('hideModal')
        },

        // 调用submit，提交
        submit() {
            this.$emit('submit')
        },

        // 用于悬浮窗位置初始化
        setStartingPoint(e) {
            this.x = e.clientX - this.node.offsetLeft
            this.y = e.clientY - this.node.offsetTop
            this.isCanMove = true
        },

        // 悬浮窗移动
        modalMove(e) {
            if (this.isCanMove) {
                this.node.style.left = e.clientX - this.x + 'px';
                this.node.style.top = e.clientY - this.y + 'px';
            } 
        },

        // 悬浮窗固定
        cancelMove() {
            this.isCanMove = false
        }
    }
}
</script>

<style scoped>
.modal-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,.5);
    z-index: 10;
}
.modal-container {
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
}
.modal-header {
    height: 56px;
    background: #409EFF;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: move;
}
.modal-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 57px;
    border-top: 1px solid #ddd;
}
.modal-footer button {
    width: 100px;
}
.modal-main {
    padding: 15px 40px;
}
</style>