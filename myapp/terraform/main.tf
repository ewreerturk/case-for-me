resource "kind_cluster" "k8s" {
    name = "project-kind"
    node_image = "kindest/node:v1.30.2"
    kind_config  {
        kind = "Cluster"
        api_version = "kind.x-k8s.io/v1alpha4"
        node {
            role = "control-plane"
          extra_port_mappings {
              container_port = 31111
              host_port      = 80
          }
        }
        node {
            role =  "worker"
        }
        node {
            role =  "worker"
        }
    }
}