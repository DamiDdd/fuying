<template>
  <div class="main">
    <div class="center rcorner">
      <div class="input">
        <p class="bigtext-blue">{{ $t("uploadgood.title") }}</p>
      </div>
      <div class="input">
        <div class="left">
          <p class="title">{{ $t("uploadgood.content") }}</p>
        </div>
        <div class="right">
          <el-input v-model="title" class="medium" clearable></el-input>
        </div>
      </div>
      <div class="input">
        <div class="left">
          <p class="title">{{ $t("uploadgood.desc") }}</p>
        </div>
        <div><el-input v-model="desc" class="medium" clearable></el-input></div>
      </div>
      <div class="input">
        <div class="left">
          <p class="title">{{ $t("uploadgood.color") }}</p>
        </div>
        <div class="right">
          <el-input
            style="width:6.25rem /* 100/16 */"
            v-model="color"
            type="color"
            class="medium"
          ></el-input>
        </div>
      </div>
      <div v-for="(item, i) in type" :key="100 + i" class="input">
        <div class="left">
          <p class="title" v-show="!notfirst(i)">
            {{ $t("uploadgood.program") }}
          </p>
        </div>
        <div class="right">
          <el-input
            :title="$t('uploadgood.program')"
            placeholder="service"
            v-model="item.name"
            class="medium"
            clearable
          ></el-input>
          <el-input
            :title="$t('uploadgood.price')"
            placeholder="price"
            v-model="item.price"
            class="medium"
            :min="0"
            oninput="if(value<0)value=0"
            type="number"
          ></el-input>
          <el-button
            class="btn"
            v-show="notfirst(i)"
            @click="deleteType(i)"
            type="danger"
            icon="el-icon-delete"
            circle
          ></el-button>
          <el-button
            class="btn"
            v-show="lastType(i)"
            @click="addType"
            type="success"
            circle
            >+</el-button
          >
        </div>
      </div>
      <div class="input last">
        <p class="title">{{ $t("uploadgood.img") }}</p>
      </div>
      <div v-for="(item, i) in imgList" :key="i" class="imgdiv">
        <h3
          class="text"
          :title="$t('uploadgood.edit')"
          v-show="!notfirst(i) || flag[i]"
          @click="flagChange(i)"
        >
          {{ item.name }}
        </h3>
        <el-input
          ref="input"
          class="titleInput"
          v-model="item.name"
          v-show="notfirst(i) && !flag[i]"
          @blur="flagChange(i)"
        ></el-input>
        <upload-img
          class="imgwin"
          ref="upload"
          :URL="uploadImgUrl"
          :limit="limit"
          :goodData="item"
          :min="min"
        ></upload-img>
        <el-button
          class="lastbtn"
          v-show="notfirst(i)"
          @click="deleteImg(i)"
          type="danger"
          icon="el-icon-delete"
          circle
        ></el-button>
        <el-button
          class="lastbtn"
          v-show="lastList(i)"
          @click="addTitle"
          type="success"
          circle
          >+</el-button
        >
      </div>
      <el-button class="submitbtn" @click="sendPic" type="primary"
        >{{ $t("uploadgood.upload")
        }}<i class="el-icon-upload el-icon--right"></i
      ></el-button>
    </div>
  </div>
</template>

<script>
import UploadImg from "common/upload/UploadImg";
import Axios from "axios";
import GLOBAL from "@/common/const";

export default {
  name: "UploadGood",
  components: {
    UploadImg
  },
  data() {
    return {
      min: 1,
      limit: 5,
      uploadImgUrl: GLOBAL.urlHead + "uploadGoodImage/",
      uploadTextUrl: GLOBAL.urlHead + "uploadGoodInfo/",
      title: "",
      desc: "",
      goodId: "",
      imgList: [{ id: "", name: this.$t("uploadgood.slider") }],
      type: [{ name: "service1", price: 0 }],
      flag: [true],
      num: 1,
      num2: 0,
      color: "#308bcc"
    };
  },
  methods: {
    // 发送图片
    sendPic() {
      let that = this;
      // part0. 判断空值
      if (this.title === "") {
        this.$message({
          type: "warning",
          message: this.$t("uploadgood.emptyinfo")
        });
        return;
      }
      // part1. 传送文字信息获取goodId
      let params = new URLSearchParams();
      params.append("title", this.title);
      params.append("desc", this.desc);
      params.append("bgColor", this.color);
      params.append("type", JSON.stringify(this.type));
      Axios.post(this.uploadTextUrl, params, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      })
        .then(function(response) {
          let data = response.data;
          console.log(data);
          // part2. 将goodId赋值给上述元素
          that.goodId = data.goodId;
          that.imgList.forEach(element => {
            element.id = data.goodId;
          });
          console.log(that.imgList);
          // part3. 调用组件方法逐个上传图片
          let refDic = that.$refs.upload;
          refDic.forEach(element => {
            // console.log(element);
            element.sendPic();
          });
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    // 增加图片组
    addTitle() {
      this.num2++;
      // 这里需要用push使得v-for实时更新
      this.imgList.push({ id: this.goodId, name: "default" + this.num2 });
      this.flag.push(true);
      console.log(this.imgList);
    },
    addType() {
      this.num++;
      let str = "service" + this.num;
      this.type.push({ name: str, price: 0 });
    },
    // 删除图片组
    deleteImg(i) {
      this.imgList.splice(i, 1);
    },
    deleteType(i) {
      this.type.splice(i, 1);
    },
    flagChange(i) {
      this.flag.splice(i, 1, !this.flag[i]);
      if (!this.flag[i]) {
        console.log(this.$refs.input);
        this.$nextTick(function() {
          this.$refs.input[i].focus();
        });
      }
    },
    // 判断是否为第一
    notfirst(i) {
      if (i !== 0) {
        return true;
      } else {
        return false;
      }
    },
    lastType(i) {
      let length = this.type.length - 1;
      if (i === length && length <= 3) {
        return true;
      } else {
        return false;
      }
    },
    // 判断是否为最末尾
    lastList(i) {
      let length = this.imgList.length - 1;
      if (i === length && length <= 3) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>

<style scoped>
.main {
  min-height: 37.5rem /* 600/16 */;
  width: 100%;
  min-width: 100rem /* 1600/16 */;
}
.center {
  min-height: 34.375rem /* 550/16 */;
  width: 90%;
  margin-left: 5%;
  margin-top: 1.25rem /* 20/16 */;
  margin-bottom: 1.25rem /* 20/16 */;
}
.imgdiv {
  border-radius: 1.5625rem /* 25/16 */;
  border: .0625rem /* 1/16 */ solid var(--theme-color);
  width: 95%;
  height: 10rem /* 160/16 */;
  display: flex;
  margin-left: 2.5%;
  margin-top: .625rem /* 10/16 */;
  margin-bottom: .625rem /* 10/16 */;
}
.titleInput {
  height: 2.5rem /* 40/16 */;
  width: 6.25rem /* 100/16 */;
  margin-top: 3.75rem /* 60/16 */;
  margin-right: .625rem /* 10/16 */;
  /* background: #000; */
}
.lastbtn {
  height: 2.5rem /* 40/16 */;
  width: 2.5rem /* 40/16 */;
  margin-top: 3.75rem /* 60/16 */;
  margin-left: .625rem /* 10/16 */;
}
.btn {
  height: 2.5rem /* 40/16 */;
  width: 2.5rem /* 40/16 */;
  margin-left: .625rem /* 10/16 */;
}
.text {
  width: 6.25rem /* 100/16 */;
  margin-top: 3.75rem /* 60/16 */;
  margin-left: .625rem /* 10/16 */;
}
.imgwin {
  margin-top: .3125rem /* 5/16 */;
}
.submitbtn {
  width: 13.75rem /* 220/16 */;
  margin-left: 43%;
  margin-top: 1.25rem /* 20/16 */;
  margin-bottom: 1.25rem /* 20/16 */;
}
.medium {
  width: 25rem /* 400/16 */;
  margin-left: 1.875rem /* 30/16 */;
}
.left {
  width: 6.25rem /* 100/16 */;
  height: 2.1875rem /* 35/16 */;
  float: left;
}
.input {
  margin-bottom: .625rem /* 10/16 */;
  margin-left: 3.125rem /* 50/16 */;
}
.left p {
  margin-left: 1.25rem /* 20/16 */;
  margin-top: .625rem /* 10/16 */;
}
.last {
  margin-top: 3.125rem /* 50/16 */;
}
</style>
