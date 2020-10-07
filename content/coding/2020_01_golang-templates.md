Title: Golang templates
Summary: Guide to golang templates from basic architectural concept to niche topics
Date: 2020-02-01
Modified: 2020-05-09
Category: Coding
Status: published


There are a few great articles that present subtopics such as 
[built-in template functions by Jon Calhoun](https://www.calhoun.io/intro-to-templates-p3-functions/)
 

This is a summarizing article with a few practical examples.

```go
import (
  "html/template"
  "net/http"
)

func index(w http.ResponseWriter, r *http.Request) {
  template.New("index").
     ParseFiles("./layout.gohtml", "./index.gohtml").
	 ExecuteTemplate(w, "layout.gohtml", map[string]interface{}{
	    "person": PersonFromRequest(r),
		"data": SomeDataClass(),
		"more_data": db.Get("SomeModel"),
	 })
}
```

The paths are relative to you binary! Usually your current working directory is the root of your Go project
but can be different.

`Template::ExecuteTemplate` receives an http response writer, file name of the template file that you want
to render and context for rendering. Each call `Template::ParseFiles(files...)` registers parsed templates
under their file name. Therefore we can use "layout.gohtml" directly in the ExecuteTemplate.

As you can see, there are two template files being parsed. The _layout file_ is simply an HTML page with
defined `blocks` that will get populated from _content template_, in our case index.gohtml, that contain
the moving blocks.

Here is solid code instead of words. First is the _layout_ file.

```html
<!doctype html><!-- layout.html -->
<html>

<head>
  <meta charset="utf-8">
  <title>{{ template "title" . }}</title>
  <link rel="stylesheet" href="/static/css/main.css">
</head>

<body>
  <script type="text/javascript" src="/static/js/jquery-3.2.1.min.js"></script>
  <nav>
	  {{if .Person.IsLoggedIn }}
		<ul><li>some</li><li>menu</li></ul>
	  {{else}}
	    <a href="/login">Login</a>
	  {{end}}
  </nav>

  {{ template "content" . }}
</body>

</html>
```

Second is the _content file_. 
```html
{{ define "title"}}Go template tutorial{{end}}

{{ define "content"}}
<div>
 some content
</div>
{{end}}
```

# Niche

## Accessing outside varible from withing a loop

Golang documentation does not say explicitely but during rendering, there is a object `$` which is
very useful - it holds all context variables. Therefore writing `{{.Person}}` and `{{$.Person}}` is
equivalent. The magic of `$` is that it works even from _loops_ where your context root changes.

Here is an example of looping over some select options of a top-level variable Goal and printing out
titles of those options while selecting the option that is selected on the model.

```html
<select>
{{range .Goal.Options }}
<option value="{{.Value}}"{{if eq .Value $.Goal.SelectedOption}} selected{{end}}>{{.Title}}</option>
{{end}}
</select>
```

## Storing something in an extra variable

My case is that I have goals in a list that I want to print out as a table. The list is sorted by Topics
and I want to print a title of a new topic when the topic changes. Thus I need to store the last topic
and compare with the current one. Behold the code below.

```html
{{$lastTopic := "" }}
<table class="highlight">
{{ range .Goals }}
{{ if ne $lastTopic .Topic }}<tr><th colspan="2">{{.Topic}}</th></tr>{{$lastTopic = .Topic}}{{end}}
<tr><td>{{.Title}} {{.Points}}</td></tr>
{{end}}
```