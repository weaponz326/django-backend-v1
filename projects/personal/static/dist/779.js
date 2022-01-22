"use strict";(self.webpackChunkfrontend_v1=self.webpackChunkfrontend_v1||[]).push([[779],{779:(te,T,i)=>{i.r(T),i.d(T,{TasksPageModule:()=>ee});var c=i(8583),m=i(2305),e=i(7716),C=i(2916),G=i(983);let w=(()=>{class o{constructor(){this.navLinks=[{text:"All Task Groups",url:"/home/tasks/all-task-groups",icon:"bi bi-list-ul"},{text:"All Task Items",url:"/home/tasks/all-task-items",icon:"bi bi-list-ul"}]}ngOnInit(){}}return o.\u0275fac=function(t){return new(t||o)},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-tasks-page"]],decls:6,vars:4,consts:[[3,"navBrand","source"],["id","wrapper"],[3,"navLinks","heading"],["id","content-wrapper",1,"d-flex","flex-column"],["id","content"]],template:function(t,n){1&t&&(e.\u0275\u0275element(0,"app-main-navbar",0),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275element(2,"app-module-sidenav",2),e.\u0275\u0275elementStart(3,"div",3),e.\u0275\u0275elementStart(4,"div",4),e.\u0275\u0275element(5,"router-outlet"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd()),2&t&&(e.\u0275\u0275property("navBrand","nR Personal")("source","Personal"),e.\u0275\u0275advance(2),e.\u0275\u0275property("navLinks",n.navLinks)("heading","Tasks"))},directives:[C.D,G.m,m.lC],styles:[""]}),o})(),E=(()=>{class o{constructor(){}ngOnInit(){}}return o.\u0275fac=function(t){return new(t||o)},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-kanban-view"]],decls:5,vars:0,consts:[[1,"row","mb-3"],[1,"col-md-12"],["routerLink","/home/tasks/view-task-group/checklist-view",1,"btn","btn-secondary","float-end","nr-standard-font"],[1,"bi","bi-arrow-left-right","me-2"]],template:function(t,n){1&t&&(e.\u0275\u0275elementStart(0,"div",0),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"button",2),e.\u0275\u0275element(3,"i",3),e.\u0275\u0275text(4," Checklist View "),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd())},directives:[m.rH],styles:["smart-kanban[_ngcontent-%COMP%]{height:400px}"]}),o})(),I=(()=>{class o{constructor(){}ngOnInit(){}}return o.\u0275fac=function(t){return new(t||o)},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-checklist-view"]],decls:5,vars:0,consts:[[1,"row","mb-3"],[1,"col-md-12"],["routerLink","/home/tasks/view-task-group/kanban-view",1,"btn","btn-secondary","float-end","nr-standard-font"],[1,"bi","bi-arrow-left-right","me-2"]],template:function(t,n){1&t&&(e.\u0275\u0275elementStart(0,"div",0),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"button",2),e.\u0275\u0275element(3,"i",3),e.\u0275\u0275text(4," Kanban View "),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd())},directives:[m.rH],styles:[""]}),o})();var p=i(8529),u=i(3810),k=i(4345),v=i(6178);const A=["connectionToastComponentReference"];let S=(()=>{class o{constructor(t){this.tasksApi=t,this.navHeading=[{text:"Dashboard",url:"/home/tasks/dashboard"}],this.allTaskGroupsCount=0,this.allTaskItemsCount=0,this.taskGroupsLineChartData=[{data:[0],label:"Task Groups"}],this.taskGroupsLineChartLabels=[""],this.taskItemsLineChartData=[{data:[0],label:"Task Items"}],this.taskItemsLineChartLabels=[""],this.chartOptions={responsive:!0,scales:{yAxes:[{beginAtZero:!0,min:0,ticks:{stepSize:1}}]}}}ngOnInit(){}ngAfterViewInit(){this.getTaskGroupsCount(),this.getTaskItemsCount(),this.getTaskGroupAnnotation(),this.getTaskItemAnnotation()}getTaskGroupsCount(){this.tasksApi.getCounts("Task Group").subscribe(t=>{console.log(t),this.allTaskGroupsCount=t},t=>{console.log(t),this.connectionToast.openToast()})}getTaskItemsCount(){this.tasksApi.getCounts("Task Item").subscribe(t=>{console.log(t),this.allTaskItemsCount=t},t=>{console.log(t),this.connectionToast.openToast()})}getTaskGroupAnnotation(){this.tasksApi.getAnnotation("Task Group").subscribe(t=>{console.log(t),this.setTaskGroupChartData(t)},t=>{console.log(t),this.connectionToast.openToast()})}getTaskItemAnnotation(){this.tasksApi.getAnnotation("Task Item").subscribe(t=>{console.log(t),this.setTaskItemChartData(t)},t=>{console.log(t),this.connectionToast.openToast()})}setTaskGroupChartData(t){this.taskGroupsLineChartLabels=[];for(let a=0;a<t.length;a++)this.taskGroupsLineChartLabels.push(t[a].date);console.log(this.taskGroupsLineChartLabels);let n=[];for(let a=0;a<t.length;a++)n.push(t[a].count);console.log(n),this.taskGroupsLineChartData=[{data:n,label:"Task Groups"}]}setTaskItemChartData(t){this.taskItemsLineChartLabels=[];for(let a=0;a<t.length;a++)this.taskItemsLineChartLabels.push(t[a].date);console.log(this.taskItemsLineChartLabels);let n=[];for(let a=0;a<t.length;a++)n.push(t[a].count);console.log(n),this.taskItemsLineChartData=[{data:n,label:"Task Items"}]}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275directiveInject(u.c))},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-dashboard"]],viewQuery:function(t,n){if(1&t&&e.\u0275\u0275viewQuery(A,5,p.Y),2&t){let a;e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.connectionToast=a.first)}},decls:41,vars:13,consts:[[3,"headings"],[1,"container"],[1,"row"],[1,"col-md-3","mb-4"],[1,"card","border-left-secondary","shadow","h-100","py-2"],[1,"card-body"],[1,"row","no-gutters","align-items-center"],[1,"col","mr-2"],[1,"text-xs","font-weight-bold","text-uppercase","mb-1"],[1,"h5","mb-0","font-weight-bold","text-gray-800"],[1,"col-md-8"],[1,"card","shadow","mb-4"],[1,"card-header","py-3","d-flex","flex-row","align-items-center","justify-content-between"],[1,"m-0","font-weight-bold"],[1,"chart-area"],["baseChart","",3,"datasets","labels","options","legend","chartType"],["connectionToastComponentReference",""]],template:function(t,n){1&t&&(e.\u0275\u0275element(0,"app-module-topnav",0),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"div",2),e.\u0275\u0275elementStart(3,"div",3),e.\u0275\u0275elementStart(4,"div",4),e.\u0275\u0275elementStart(5,"div",5),e.\u0275\u0275elementStart(6,"div",6),e.\u0275\u0275elementStart(7,"div",7),e.\u0275\u0275elementStart(8,"div",8),e.\u0275\u0275text(9,"All Task Groups"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(10,"div",9),e.\u0275\u0275text(11),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(12,"div",3),e.\u0275\u0275elementStart(13,"div",4),e.\u0275\u0275elementStart(14,"div",5),e.\u0275\u0275elementStart(15,"div",6),e.\u0275\u0275elementStart(16,"div",7),e.\u0275\u0275elementStart(17,"div",8),e.\u0275\u0275text(18,"All Task Items"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(19,"div",9),e.\u0275\u0275text(20),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(21,"div",2),e.\u0275\u0275elementStart(22,"div",10),e.\u0275\u0275elementStart(23,"div",11),e.\u0275\u0275elementStart(24,"div",12),e.\u0275\u0275elementStart(25,"h6",13),e.\u0275\u0275text(26,"Total Task Groups by Day"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(27,"div",5),e.\u0275\u0275elementStart(28,"div",14),e.\u0275\u0275element(29,"canvas",15),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(30,"div",2),e.\u0275\u0275elementStart(31,"div",10),e.\u0275\u0275elementStart(32,"div",11),e.\u0275\u0275elementStart(33,"div",12),e.\u0275\u0275elementStart(34,"h6",13),e.\u0275\u0275text(35,"Total Task Items by Day"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(36,"div",5),e.\u0275\u0275elementStart(37,"div",14),e.\u0275\u0275element(38,"canvas",15),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(39,"app-connection-toast",null,16)),2&t&&(e.\u0275\u0275property("headings",n.navHeading),e.\u0275\u0275advance(11),e.\u0275\u0275textInterpolate(n.allTaskGroupsCount),e.\u0275\u0275advance(9),e.\u0275\u0275textInterpolate(n.allTaskItemsCount),e.\u0275\u0275advance(9),e.\u0275\u0275property("datasets",n.taskGroupsLineChartData)("labels",n.taskGroupsLineChartLabels)("options",n.chartOptions)("legend",!0)("chartType","line"),e.\u0275\u0275advance(9),e.\u0275\u0275property("datasets",n.taskItemsLineChartData)("labels",n.taskItemsLineChartLabels)("options",n.chartOptions)("legend",!0)("chartType","line"))},directives:[k.H,v.jh,p.Y],styles:[""]}),o})();var l=i(3679);const D=["buttonElementReference"],P=["connectionToastComponentReference"];let b=(()=>{class o{constructor(t,n){this.router=t,this.tasksApi=n,this.taskGroupForm=new l.cw({})}ngOnInit(){this.initTaskForm()}openModal(){this.buttonElement.nativeElement.click()}initTaskForm(){this.taskGroupForm=new l.cw({taskGroupName:new l.NI("")})}postTaskGroup(){let t={user:localStorage.getItem("personal_id"),task_group:this.taskGroupForm.controls.taskGroupName.value};console.log(t)}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275directiveInject(m.F0),e.\u0275\u0275directiveInject(u.c))},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-new-task-group"]],viewQuery:function(t,n){if(1&t&&(e.\u0275\u0275viewQuery(D,5,e.ElementRef),e.\u0275\u0275viewQuery(P,5,p.Y)),2&t){let a;e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.buttonElement=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.connectionToast=a.first)}},decls:25,vars:2,consts:[["data-bs-toggle","modal","data-bs-target","#newTaskGroupModal",3,"hidden"],["buttonElementReference",""],["id","newTaskGroupModal","tabindex","-1","aria-labelledby","newTaskGroupModalLabel","aria-hidden","true",1,"modal","fade","form-modal"],[1,"modal-dialog"],[1,"modal-content"],[1,"page-form",3,"formGroup","ngSubmit"],[1,"modal-header","bg-light"],["id","newTaskGroupModalLabel",1,"modal-title"],["type","button","data-bs-dismiss","modal","aria-label","Close",1,"btn-close"],[1,"modal-body"],[1,"row","mb-1"],[1,"col-md-4"],[1,"float-end","mt-1"],[1,"col-md-8"],["formControlName","taskGroupName",1,"form-control","form-control-sm","w-100"],[1,"modal-footer"],["type","submit","data-bs-dismiss","modal",1,"btn","btn-sm","btn-secondary","modal-form-btn"],["type","button","data-bs-dismiss","modal",1,"btn","btn-sm","btn-secondary","modal-form-btn"],["connectionToastComponentReference",""]],template:function(t,n){1&t&&(e.\u0275\u0275elementStart(0,"button",0,1),e.\u0275\u0275text(2," Launch demo modal\n"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(3,"div",2),e.\u0275\u0275elementStart(4,"div",3),e.\u0275\u0275elementStart(5,"div",4),e.\u0275\u0275elementStart(6,"form",5),e.\u0275\u0275listener("ngSubmit",function(){return n.postTaskGroup()}),e.\u0275\u0275elementStart(7,"div",6),e.\u0275\u0275elementStart(8,"span",7),e.\u0275\u0275text(9,"Add New Task Group"),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(10,"button",8),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(11,"div",9),e.\u0275\u0275elementStart(12,"div",10),e.\u0275\u0275elementStart(13,"div",11),e.\u0275\u0275elementStart(14,"label",12),e.\u0275\u0275text(15,"Task Group Name :"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(16,"div",13),e.\u0275\u0275element(17,"input",14),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(18,"div",15),e.\u0275\u0275elementStart(19,"button",16),e.\u0275\u0275text(20,"Save"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(21,"button",17),e.\u0275\u0275text(22,"Cancel"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(23,"app-connection-toast",null,18)),2&t&&(e.\u0275\u0275property("hidden",!0),e.\u0275\u0275advance(6),e.\u0275\u0275property("formGroup",n.taskGroupForm))},directives:[l._Y,l.JL,l.sg,l.Fj,l.JJ,l.u,p.Y],styles:[""]}),o})();var h=i(3203),d=i(4289),R=i(490);let _=(()=>{class o{constructor(t,n){this.pdfPrint=t,this.tasksApi=n,this.taskGroupsGridData=[],this.taskItemsGridData=[]}getPrintTaskGroups(t){this.tasksApi.getTaskGroups(1,t,"").subscribe(n=>{console.log(n),this.taskGroupsGridData=n.results,this.printAllTaskGroups()},n=>{console.log(n)})}printAllTaskGroups(){let t=this.taskGroupsGridData.map(function(s){return{task_group:s.task_group,created_at:new Date(s.created_at).toISOString().slice(0,16)}});var n=[["Task Group","Created At"]];t.forEach(s=>{var g=[];for(let f in s)g.push(s[f]);n.push(g)}),this.pdfPrint.openPdf([{layout:"lightHorizontalLines",table:{headerRows:1,widths:["65%","35%"],body:n}}])}getPrintAllTaskItems(t){this.tasksApi.getAllTaskItems(1,t,"").subscribe(n=>{console.log(n),this.taskItemsGridData=n.results,this.printAllTaskItems()},n=>{console.log(n)})}printAllTaskItems(){let t=this.taskItemsGridData.map(function(s){return{task_item:s.task_item,priority:s.priority,start_date:new Date(s.start_date).toISOString().slice(0,16),end_date:new Date(s.end_date).toISOString().slice(0,16),status:s.status}});var n=[["Task Item","Priority","Start Date","End Date","Status"]];t.forEach(s=>{var g=[];for(let f in s)g.push(s[f]);n.push(g)}),this.pdfPrint.openPdf([{layout:"lightHorizontalLines",table:{headerRows:1,widths:["36%","14%","18%","18%","14%"],body:n}}])}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275inject(R.n),e.\u0275\u0275inject(u.c))},o.\u0275prov=e.\u0275\u0275defineInjectable({token:o,factory:o.\u0275fac,providedIn:"root"}),o})();const F=["connectionToastComponentReference"],Q=["newTaskGroupComponentReference"],L=["tablePaginationComponentReference"],V=["taskGroupSortingComponentReference"],x=["createdAtSortingComponentReference"];function N(o,r){if(1&o){const t=e.\u0275\u0275getCurrentView();e.\u0275\u0275elementStart(0,"tr",20),e.\u0275\u0275listener("dblclick",function(){const s=e.\u0275\u0275restoreView(t).$implicit;return e.\u0275\u0275nextContext().viewTaskGroup(s.id)}),e.\u0275\u0275elementStart(1,"td"),e.\u0275\u0275text(2),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(3,"td"),e.\u0275\u0275text(4),e.\u0275\u0275pipe(5,"date"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd()}if(2&o){const t=r.$implicit;e.\u0275\u0275advance(2),e.\u0275\u0275textInterpolate(null==t?null:t.task_group),e.\u0275\u0275advance(2),e.\u0275\u0275textInterpolate(e.\u0275\u0275pipeBind1(5,2,null==t?null:t.created_at))}}let M=(()=>{class o{constructor(t,n,a){this.router=t,this.tasksApi=n,this.tasksPrint=a,this.navHeading=[{text:"All Task Groups",url:"/home/tasks/all-task-groups"}],this.taskGroupsGridData=[],this.currentPage=0,this.totalPages=0,this.totalItems=0}ngOnInit(){}ngAfterViewInit(){this.getTaskGroups(1,20,"")}getTaskGroups(t,n,a){this.tasksApi.getTaskGroups(t,n,a).subscribe(s=>{console.log(s),this.taskGroupsGridData=s.results,this.currentPage=s.current_page,this.totalPages=s.total_pages,this.totalItems=s.count},s=>{console.log(s),this.connectionToast.openToast()})}viewTaskGroup(t){console.log(t),sessionStorage.setItem("personal_task_group_id",t),this.router.navigateByUrl("/home/tasks/view-task-group/kanban-view")}sortTable(t){console.log(t),this.getTaskGroups(1,20,t),"task_group"==t||"-task_group"==t?this.createdAtSorting.resetSort():("created_at"==t||"-created_at"==t)&&this.taskGroupSorting.resetSort()}onPrint(){console.log("lets start printing..."),this.tasksPrint.getPrintTaskGroups(this.totalItems)}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275directiveInject(m.F0),e.\u0275\u0275directiveInject(u.c),e.\u0275\u0275directiveInject(_))},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-all-task-groups"]],viewQuery:function(t,n){if(1&t&&(e.\u0275\u0275viewQuery(F,5,p.Y),e.\u0275\u0275viewQuery(Q,5,b),e.\u0275\u0275viewQuery(L,5,h.Q),e.\u0275\u0275viewQuery(V,5,d.m),e.\u0275\u0275viewQuery(x,5,d.m)),2&t){let a;e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.connectionToast=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.newTaskGroup=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.tablePagination=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.taskGroupSorting=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.createdAtSorting=a.first)}},decls:30,vars:7,consts:[[3,"headings","showPrint","print"],[1,"container"],[1,"row","mb-3"],[1,"col-md-12"],[1,"btn","btn-secondary","page-add-btn",3,"click"],[1,"row"],[1,"col-md-7"],[1,"table","table-bordered","table-sm","w-100","page-table"],[1,"bg-light"],["width","65%"],[3,"sortField","sortDirection"],["taskGroupSortingComponentReference",""],["width","35%"],["createdAtSortingComponentReference",""],["class","table-pointer",3,"dblclick",4,"ngFor","ngForOf"],["colspan","2"],[3,"currentPage","totalPages","pageSelected"],["tablePaginationComponentReference",""],["newTaskGroupComponentReference",""],["connectionToastComponentReference",""],[1,"table-pointer",3,"dblclick"]],template:function(t,n){1&t&&(e.\u0275\u0275elementStart(0,"app-module-topnav",0),e.\u0275\u0275listener("print",function(){return n.onPrint()}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"div",2),e.\u0275\u0275elementStart(3,"div",3),e.\u0275\u0275elementStart(4,"button",4),e.\u0275\u0275listener("click",function(){return n.newTaskGroup.openModal()}),e.\u0275\u0275text(5,"New Task Group"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(6,"div",5),e.\u0275\u0275elementStart(7,"div",6),e.\u0275\u0275elementStart(8,"table",7),e.\u0275\u0275elementStart(9,"thead"),e.\u0275\u0275elementStart(10,"tr",8),e.\u0275\u0275elementStart(11,"th",9),e.\u0275\u0275text(12," Task Group Name "),e.\u0275\u0275elementStart(13,"app-table-sorting",10,11),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(15,"th",12),e.\u0275\u0275text(16," Created At "),e.\u0275\u0275elementStart(17,"app-table-sorting",10,13),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(19,"tbody"),e.\u0275\u0275template(20,N,6,4,"tr",14),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(21,"tfoot"),e.\u0275\u0275elementStart(22,"tr",8),e.\u0275\u0275elementStart(23,"td",15),e.\u0275\u0275elementStart(24,"app-table-pagination",16,17),e.\u0275\u0275listener("pageSelected",function(s){return n.getTaskGroups(s,20,"")}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(26,"app-new-task-group",null,18),e.\u0275\u0275element(28,"app-connection-toast",null,19)),2&t&&(e.\u0275\u0275property("headings",n.navHeading)("showPrint",!0),e.\u0275\u0275advance(13),e.\u0275\u0275property("sortField","task_group"),e.\u0275\u0275advance(4),e.\u0275\u0275property("sortField","created_at"),e.\u0275\u0275advance(3),e.\u0275\u0275property("ngForOf",n.taskGroupsGridData),e.\u0275\u0275advance(4),e.\u0275\u0275property("currentPage",n.currentPage)("totalPages",n.totalPages))},directives:[k.H,d.m,c.sg,h.Q,b,p.Y],pipes:[c.uU],styles:[""]}),o})();const j=["connectionToastComponentReference"],O=["tablePaginationComponentReference"],H=["taskItemSortingComponentReference"],Y=["prioritySortingComponentReference"],B=["startDateSortingComponentReference"],z=["endDateSortingComponentReference"],J=["statusSortingComponentReference"];function K(o,r){if(1&o&&(e.\u0275\u0275elementStart(0,"tr"),e.\u0275\u0275elementStart(1,"td"),e.\u0275\u0275text(2),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(3,"td"),e.\u0275\u0275text(4),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(5,"td"),e.\u0275\u0275text(6),e.\u0275\u0275pipe(7,"date"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(8,"td"),e.\u0275\u0275text(9),e.\u0275\u0275pipe(10,"date"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(11,"td"),e.\u0275\u0275text(12),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd()),2&o){const t=r.$implicit;e.\u0275\u0275advance(2),e.\u0275\u0275textInterpolate(null==t?null:t.task_item),e.\u0275\u0275advance(2),e.\u0275\u0275textInterpolate(null==t?null:t.priority),e.\u0275\u0275advance(2),e.\u0275\u0275textInterpolate(e.\u0275\u0275pipeBind1(7,5,null==t?null:t.start_date)),e.\u0275\u0275advance(3),e.\u0275\u0275textInterpolate(e.\u0275\u0275pipeBind1(10,7,null==t?null:t.end_date)),e.\u0275\u0275advance(3),e.\u0275\u0275textInterpolate(null==t?null:t.status)}}let U=(()=>{class o{constructor(t,n){this.tasksApi=t,this.tasksPrint=n,this.navHeading=[{text:"All Task Items",url:"/home/tasks/all-task-items"}],this.taskItemsGridData=[],this.currentPage=0,this.totalPages=0,this.totalItems=0}ngOnInit(){}ngAfterViewInit(){this.getAllTaskItems(1,20,"")}getAllTaskItems(t,n,a){this.tasksApi.getAllTaskItems(t,n,a).subscribe(s=>{console.log(s),this.taskItemsGridData=s.results,this.currentPage=s.current_page,this.totalPages=s.total_pages,this.totalItems=s.count},s=>{console.log(s),this.connectionToast.openToast()})}sortTable(t){console.log(t),this.getAllTaskItems(1,20,t),"taskItem"==t||"-taskItem"==t?(this.prioritySorting.resetSort(),this.startDateSorting.resetSort(),this.endDateSorting.resetSort(),this.statusSorting.resetSort()):"priority"==t||"-priority"==t?(this.taskItemSorting.resetSort(),this.startDateSorting.resetSort(),this.endDateSorting.resetSort(),this.statusSorting.resetSort()):"start_date"==t||"-start_date"==t?(this.taskItemSorting.resetSort(),this.prioritySorting.resetSort(),this.endDateSorting.resetSort(),this.statusSorting.resetSort()):"end_date"==t||"-end_date"==t?(this.taskItemSorting.resetSort(),this.prioritySorting.resetSort(),this.startDateSorting.resetSort(),this.statusSorting.resetSort()):("status"==t||"-status"==t)&&(this.taskItemSorting.resetSort(),this.prioritySorting.resetSort(),this.startDateSorting.resetSort(),this.endDateSorting.resetSort())}onPrint(){console.log("lets start printing..."),this.tasksPrint.getPrintAllTaskItems(this.totalItems)}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275directiveInject(u.c),e.\u0275\u0275directiveInject(_))},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-all-task-items"]],viewQuery:function(t,n){if(1&t&&(e.\u0275\u0275viewQuery(j,5,p.Y),e.\u0275\u0275viewQuery(O,5,h.Q),e.\u0275\u0275viewQuery(H,5,d.m),e.\u0275\u0275viewQuery(Y,5,d.m),e.\u0275\u0275viewQuery(B,5,d.m),e.\u0275\u0275viewQuery(z,5,d.m),e.\u0275\u0275viewQuery(J,5,d.m)),2&t){let a;e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.connectionToast=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.tablePagination=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.taskItemSorting=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.prioritySorting=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.startDateSorting=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.endDateSorting=a.first),e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.statusSorting=a.first)}},decls:36,vars:10,consts:[[3,"headings","showPrint","print"],[1,"container"],[1,"row"],[1,"col-md-10"],[1,"table","table-bordered","table-sm","w-100","page-table"],[1,"bg-light"],["width","36%"],[3,"sortField","sortDirection"],["taskItemSortingComponentReference",""],["width","14%"],["prioritySortingComponentReference",""],["width","18%"],["startDateSortingComponentReference",""],["endDateSortingComponentReference",""],["statusSortingComponentReference",""],[4,"ngFor","ngForOf"],["colspan","5"],[3,"currentPage","totalPages","pageSelected"],["tablePaginationComponentReference",""],["connectionToastComponentReference",""]],template:function(t,n){1&t&&(e.\u0275\u0275elementStart(0,"app-module-topnav",0),e.\u0275\u0275listener("print",function(){return n.onPrint()}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"div",2),e.\u0275\u0275elementStart(3,"div",3),e.\u0275\u0275elementStart(4,"table",4),e.\u0275\u0275elementStart(5,"thead"),e.\u0275\u0275elementStart(6,"tr",5),e.\u0275\u0275elementStart(7,"th",6),e.\u0275\u0275text(8," Task Item "),e.\u0275\u0275elementStart(9,"app-table-sorting",7,8),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(11,"th",9),e.\u0275\u0275text(12," Priority "),e.\u0275\u0275elementStart(13,"app-table-sorting",7,10),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(15,"th",11),e.\u0275\u0275text(16," Start Date "),e.\u0275\u0275elementStart(17,"app-table-sorting",7,12),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(19,"th",11),e.\u0275\u0275text(20," End Date "),e.\u0275\u0275elementStart(21,"app-table-sorting",7,13),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(23,"th",9),e.\u0275\u0275text(24," Status "),e.\u0275\u0275elementStart(25,"app-table-sorting",7,14),e.\u0275\u0275listener("sortDirection",function(s){return n.sortTable(s)}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(27,"tbody"),e.\u0275\u0275template(28,K,13,9,"tr",15),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(29,"tfoot"),e.\u0275\u0275elementStart(30,"tr",5),e.\u0275\u0275elementStart(31,"td",16),e.\u0275\u0275elementStart(32,"app-table-pagination",17,18),e.\u0275\u0275listener("pageSelected",function(s){return n.getAllTaskItems(s,20,"")}),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(34,"app-connection-toast",null,19)),2&t&&(e.\u0275\u0275property("headings",n.navHeading)("showPrint",!0),e.\u0275\u0275advance(9),e.\u0275\u0275property("sortField","task_item"),e.\u0275\u0275advance(4),e.\u0275\u0275property("sortField","priority"),e.\u0275\u0275advance(4),e.\u0275\u0275property("sortField","start_date"),e.\u0275\u0275advance(4),e.\u0275\u0275property("sortField","endDate"),e.\u0275\u0275advance(4),e.\u0275\u0275property("sortField","status"),e.\u0275\u0275advance(3),e.\u0275\u0275property("ngForOf",n.taskItemsGridData),e.\u0275\u0275advance(4),e.\u0275\u0275property("currentPage",n.currentPage)("totalPages",n.totalPages))},directives:[k.H,d.m,c.sg,h.Q,p.Y],pipes:[c.uU],styles:[""]}),o})();const $=["connectionToastComponentReference"],X=[{path:"",component:w,children:[{path:"",component:S},{path:"dashboard",component:S},{path:"all-task-groups",component:M},{path:"view-task-group",component:(()=>{class o{constructor(t){this.tasksApi=t,this.navHeading=[{text:"View Task Group",url:"/home/tasks/view-task-group"}],this.taskGroupForm=new l.cw({}),this.taskGroupFormData=[],this.isTaskGroupSaving=!1}ngOnInit(){this.initTaskGroupForm()}ngAfterViewInit(){this.getTaskGroup()}initTaskGroupForm(){this.taskGroupForm=new l.cw({taskGroupName:new l.NI("")})}getTaskGroup(){this.tasksApi.getSingleTaskGroup().subscribe(t=>{console.log(t),this.taskGroupForm.controls.taskGroupName.setValue(t.task_group)},t=>{console.log(t),this.connectionToast.openToast()})}putTaskGroup(){let t={user:localStorage.getItem("personal_id"),task_roup:this.taskGroupForm.controls.taskGroupName.value};console.log(t),this.isTaskGroupSaving=!0,this.tasksApi.putTaskGroup(t).subscribe(n=>{console.log(n),this.isTaskGroupSaving=!1},n=>{console.log(n),this.connectionToast.openToast(),this.isTaskGroupSaving=!1})}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275directiveInject(u.c))},o.\u0275cmp=e.\u0275\u0275defineComponent({type:o,selectors:[["app-view-task-group"]],viewQuery:function(t,n){if(1&t&&e.\u0275\u0275viewQuery($,5,p.Y),2&t){let a;e.\u0275\u0275queryRefresh(a=e.\u0275\u0275loadQuery())&&(n.connectionToast=a.first)}},decls:18,vars:4,consts:[[3,"headings","showPrint"],[1,"container"],[1,"row","page-form"],[1,"col-md-9"],[1,"page-form",3,"formGroup","ngSubmit"],[1,"row","mb-3"],[1,"col-md-3"],[1,"float-end","mt-1"],[1,"col-md-6"],["formControlName","taskGroupName",1,"form-control","form-control-sm","w-100"],["type","submit",1,"btn","btn-sm","btn-secondary","page-form-btn",3,"disabled"],["connectionToastComponentReference",""]],template:function(t,n){1&t&&(e.\u0275\u0275element(0,"app-module-topnav",0),e.\u0275\u0275elementStart(1,"div",1),e.\u0275\u0275elementStart(2,"div",2),e.\u0275\u0275elementStart(3,"div",3),e.\u0275\u0275elementStart(4,"form",4),e.\u0275\u0275listener("ngSubmit",function(){return n.putTaskGroup()}),e.\u0275\u0275elementStart(5,"div",5),e.\u0275\u0275elementStart(6,"div",6),e.\u0275\u0275elementStart(7,"label",7),e.\u0275\u0275text(8,"Task Group Name :"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(9,"div",8),e.\u0275\u0275element(10,"input",9),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementStart(11,"div",6),e.\u0275\u0275elementStart(12,"button",10),e.\u0275\u0275text(13,"Save"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(14,"hr"),e.\u0275\u0275elementEnd(),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(15,"router-outlet"),e.\u0275\u0275elementEnd(),e.\u0275\u0275element(16,"app-connection-toast",null,11)),2&t&&(e.\u0275\u0275property("headings",n.navHeading)("showPrint",!0),e.\u0275\u0275advance(4),e.\u0275\u0275property("formGroup",n.taskGroupForm),e.\u0275\u0275advance(8),e.\u0275\u0275property("disabled",n.isTaskGroupSaving))},directives:[k.H,l._Y,l.JL,l.sg,l.Fj,l.JJ,l.u,m.lC,p.Y],styles:[""]}),o})(),canActivate:[(()=>{class o{constructor(t){this.router=t}canActivate(t){return!!sessionStorage.getItem("personal_task_group_id")||(this.router.navigateByUrl("/home/tasks"),!1)}}return o.\u0275fac=function(t){return new(t||o)(e.\u0275\u0275inject(m.F0))},o.\u0275prov=e.\u0275\u0275defineInjectable({token:o,factory:o.\u0275fac,providedIn:"root"}),o})()],children:[{path:"kanban-view",component:E},{path:"checklist-view",component:I}]},{path:"all-task-items",component:U}]}];let Z=(()=>{class o{}return o.\u0275fac=function(t){return new(t||o)},o.\u0275mod=e.\u0275\u0275defineNgModule({type:o}),o.\u0275inj=e.\u0275\u0275defineInjector({imports:[[m.Bz.forChild(X)],m.Bz]}),o})();var q=i(6305),y=i(2743);let W=(()=>{class o{}return o.\u0275fac=function(t){return new(t||o)},o.\u0275mod=e.\u0275\u0275defineNgModule({type:o}),o.\u0275inj=e.\u0275\u0275defineInjector({imports:[[c.ez,m.Bz,l.u5,l.UX,v.m9,y.p]]}),o})(),ee=(()=>{class o{}return o.\u0275fac=function(t){return new(t||o)},o.\u0275mod=e.\u0275\u0275defineNgModule({type:o}),o.\u0275inj=e.\u0275\u0275defineInjector({imports:[[c.ez,Z,q.M,y.p,W]]}),o})()}}]);