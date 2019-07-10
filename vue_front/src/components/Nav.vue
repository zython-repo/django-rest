<template>
	<div class="Move_buttons">
		<div class="buttons-wrap">
			<div class="buttons">
				<div class="front">
					<img :src="beans">
				</div>
				<div class="back" v-on:click="change('search')">
					<div>
						<h3>search</h3>
					</div>
				</div>
			</div>
		</div>
		<div class="buttons-wrap">
			<div class="buttons">
				<div class="front">
					<img :src="grinder">
				</div>
				<div class="back" v-on:click="change('parse')">
					<div>
						<h3>parse</h3>
					</div>
				</div>
			</div>
		</div>
		<div class="buttons-wrap">
			<div class="buttons">
				<div class="front">
					<img :src="coffee">
				</div>
				<div class="back" v-on:click="change('hi')">
					<div>
						<h3>hi</h3>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'NavBtn',
		data() {
			return{
				beans: require('../assets/beans.png'),
				grinder: require('../assets/grinder.png'),
				coffee: require('../assets/handdrip.png'),
				listType: ''
			}
		},
		methods: {
			change(type) {
				this.listType = type;
				this.$emit('get_type', type);
			}
		},
	}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.Move_buttons {
	position: absolute;
	width: 0%;
	right: 15%;
}
.buttons-wrap {
	position: relative;
	width: 150px; height: 150px; right: 10px;
	float: left;
	display: flex;
	justify-content: center;
	align-items: center;
	perspective: 1000px;
}
.buttons {
	position: relative;
	width: 150px; height: 150px;
}
.buttons img {
	width: 100%;
	padding: 15px;
	transition: all 0.6s ease 0.2s;
	border: 1.45px solid #BE800E;
	border-radius: 10px;
}
.buttons div {
	position: absolute;
	bottom: 0%; left: 0;
	width: 100%;
	height: 100%;
	padding: 10% 10% 0% 10%;
	box-sizing: border-box;
	z-index: 1;
	line-height: 1.7em;
	color: #BE800E;
	font-size: 20px;
	opacity:1;
	transition: all 0.5s ease;
}
.buttons div h3 {
	font-family: 'Indie Flower', cursive;
	font-weight: 600;
	text-transform: uppercase;
	font-size: 24px;
	position: relative;
	top: 50px;
	height: 80px;
}
.buttons .front {
	position: absolute; left: 0; top: 0;
		transform : rotateY(0deg);
		width : 100%;
		height : 100%;
		cursor : pointer;
	z-index: 10;
		transition : transform 1s;
		backface-visibility : hidden;
}
.buttons .back {
	position: absolute; left: 0; top: 0;
		transform : rotateY(-180deg);
		width : 100%;
		height : 100%;
		cursor : pointer;
		transition : transform 1s;
		backface-visibility : hidden;
}
.buttons:hover .front {
	transform : rotateY(180deg)
}

.buttons:hover .back {
	transform : rotateY(0);
}
</style>

