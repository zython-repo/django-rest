<template>
	<div class='Main_Home'>
		<Top></Top>
		<div class='search_bar' v-show="listType === 'search'">
			<input type="text" v-model="searchKey" v-on:keyup="getSearch" placeholder="search title!" />
		</div>
		<div class='parsing_bar' v-show="listType === 'parse'">
			<div class="parsing_title">
				{{ title }}
			</div>
			<setFile class='main_parse' @load='getParse'></setFile>
		</div>
		<div class='' v-show="listType === 'hi'">
			Handshake only
		</div>
		<div class='talk_style'>
			<div class='chat' v-for='list in lists' :key='list.pk'>
				<h2>
					<router-link
						:to='{ name: "Detail", params: { tag: list.tag } }'
						class='list-link'>
						{{ list.title }}
					</router-link>
					{{ list.body }}
				</h2>
			</div>
			<div class='paging'>
				<p v-show='loadingLists'>...loading...</p>
				<button
					v-show='next'
					@click='getGoal'
					class='btn btn-more'
					>Load More
				</button>
			</div>
		</div>
		<NavBtn @get_type='parentChange'></NavBtn>
	</div>
</template>

<script>
	import { apiService } from '@/common/api.service.js';
import Top from '@/components/Join.vue'
import NavBtn from '@/components/Nav.vue'
import setFile from '@/components/Parsing_Bar.vue'

export default {
	name: 'Main',
	components: {
		Top,
		NavBtn,
		setFile
	},
	data() {
		return {
			lists: [],
			next: null,
			loadingLists: false,
			listType: '',
			searchKey: '',
			title: ''
		}
	},
	methods: {
		getLists() {
			this.lists = [];
			this.next = null;
			let endpoint = '/api/rest_back/';
			this.getGoal(endpoint)
		},
		getSearch() {
			this.lists = [];
			this.next = null;	
			let endpoint = `/api/rest_back/?search=${this.searchKey}`;
			this.getGoal(endpoint)
		},
		getParse(title) {
			this.title = title;
			this.lists = [];
			this.next = null;	
			let endpoint = `/api/rest_back/?search=${this.title}`;
			this.getGoal(endpoint)
		},
		getGoal(endpoint) {
			if (this.next) {
				endpoint = this.next;
			}
			this.loadingLists = true;
			apiService(endpoint)
				.then(data => {
					this.lists.push(...data.results)
					this.loadingLists = false;
					if (data.next) {
						this.next = data.next;
					} else {
						this.next = null;
					}
				})
		},
		parentChange(listType) {
			this.listType = listType;
			this.searchKey = '',
			this.title = ''
			this.getLists()
		},
	},
	created() {
		this.getLists()
	},
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

.talk_style {
	border: 4px double #BE800E;
	border-radius: 7px;
	width: 80%;
	height: 100%;
	position: relative;
	left: 20px;
	top: 15px;
	float: left;
}
.search_bar {
}
.main_parse {
	position: initial;
}
.parse_result {
	position: relative;
	z-index: 5;
	top: 40px;
	font-size: 30px;
	font-weight: 800;
	color: #ecad39;
}
.parsing_title {
	font-family: 'Indie Flower', cursive;
}
.top_menu {
	position: relative;
	padding-bottom: 20px;

}
.chat {
	position: relative;
	padding-left: 15px;
	text-align: left;
	top: 10px;
}
.list-link {
	color: #BE800E;
}
.list-link:hover {
	text-decoration: none;
	background-color: #BE800E;
	color: #fff;
	position: relative;
	padding-left: 11px;
	border-radius: 10px;
	bottom: 6px;
}
.paging {
	padding-bottom: 10px;
}
.btn {
	display: inline-block;
	margin: 6px;
	font-size: inherit;
	line-height: 1.42;
	padding: 0.6em 1.6em;
	font-weight: 600;
	border-width: 0;
	border-style: solid;
	background: transparent;
	border-radius: 0.5em;
	cursor: pointer;
	font-family: 'Indie Flower', cursive;
	user-select: none;
	vertical-align: bottom;
	transition: box-shadow 0.2s, transform 0.2s;
	border-radius: 12%/50%;
	box-shadow: 0 0 0 1px #BE800E;
}
.btn-more {
	color: #BE800E;
}
.btn-more:hover {
	color: #BE800E;
	box-shadow: 0 1px 10px 1px #BE800E;
}
.btn-more:active {
	box-shadow: 0 2px 6px 1px #BE800E inset;
	transition-duration: 0.05s;
}
</style>
