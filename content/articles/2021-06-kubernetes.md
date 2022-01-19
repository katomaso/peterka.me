Title: Kubernetes (on Azure) and setting up Gitlab CD
Date: 2021-06-02
Category: Articles
Summary: Some kubernetes gotchas we encountered in Mall.cz. Recently, we migrated to a new kubernetes. Other cloud providers have more pleasant experience when building k8s cloud but Azure is alright.

What I like in Mall.cz is that we try to keep our consumption as low as possible. Therefore the biggest complaint I have
against Azure is that it's extremely hard to 
 1) know what HW capabilities your machines have (you have to use price calculator to see the HW specs)
 2) to see load of all your nodes and their free space
 
In order to see how are nodes are utilized, Petr found https://github.com/etopeter/kubectl-view-utilization. Now we can
see the utilization broken down by nodes `kubectl view-utilization nodes` and by namespaces!

But this gives you only the summary of your limits but not the actual load of the system. Please, put your hands together
for `kubectl top pods` and `kubectl top nodes`.


## Setting up CD from Gitlab to Azure

Setting up CD to azure was not that bad in the end. We have CD linked to git tags. Therefore we needed to create a 
`ServiceAccount` for gitlab CD. 

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: gitlab-deployment-account
  namespace: mall-cz
```

This account needs to have permission to list and modify pods, deployments and services. Also, it is necessary to
gather all API Groups - that gitlab will use. API group is the first thing after / in `apiVersion`. If there is none,
then giving "" into `group` is still mandatory. We have one `apps/v1` for Deployment specification, so "apps" went to
allowed groups as well.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: gitlab-deployer
  namespace: my-namespace
rules:
  - apiGroups: ["", "apps"]
    resources: ["pods", "deployments", "services"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

In the end, you need to create a `RoleBinding` between the `ServiceAccount` and `Role`.

Gitlab then needs a token so it can issue commands to kube API via kubectl. The token can be found in k8s secrets. It 
is created automatically by service account manager. It has type of `kubernetes.io/service-account-token` and is named 
`<your-service-account>-token-<random-string>`. It is annotated with account's name in `kubernetes.io/service-account.name`
and contains all necessary credentials in its value.

Second, we need the kubernetes daemon to be able to pull our containers from Gitlab's container repository. So we give
it access using a dockerconfigjson secret.

```yaml
apiVersion: v1
data:
  .dockerconfigjson: <base64 encoded JSON {"auths":{"registry.gitlab.com":{"password":"<pass>","username":"<uname>"}}}>
kind: Secret
metadata:
  name: gitlab
  namespace: mall-cz
type: kubernetes.io/dockerconfigjson
```
